import sys
import signal
import requests
from xml.etree.ElementTree import VERSION
from datetime import datetime
from cachetools import TTLCache
from functools import wraps
from threading import Timer
from django.http import JsonResponse


KABLE_ENVIRONMENT_HEADER_KEY = 'KABLE-ENVIRONMENT'
KABLE_CLIENT_ID_HEADER_KEY = 'KABLE-CLIENT-ID'
KABLE_CLIENT_SECRET_HEADER_KEY = 'KABLE-CLIENT-SECRET'
X_CLIENT_ID_HEADER_KEY = 'X-CLIENT-ID'
X_API_KEY_HEADER_KEY = 'X-API-KEY'


class Kable:

    def __init__(self, config):

        print("Initializing Kable")

        if config is None:
            raise RuntimeError(
                "Failed to initialize Kable: config not provided")

        if "environment" not in config:
            raise RuntimeError(
                'Failed to initialize Kable: environment not provided')

        if "client_id" not in config:
            raise RuntimeError(
                'Failed to initialize Kable: client_id not provided')

        if "client_secret" not in config:
            raise RuntimeError(
                'Failed to initialize Kable: client_secret not provided')

        if "base_url" not in config:
            raise RuntimeError(
                'Failed to initialize Kable: base_url not provided')

        self.environment = config["environment"]
        self.kableClientId = config["client_id"]
        self.kableClientSecret = config["client_secret"]
        self.baseUrl = config["base_url"]

        if "debug" in config:
            self.debug = config["debug"]
            if self.debug:
                print("Starting Kable with debug enabled")
        else:
            self.debug = False

        if "recordAuthentication" in config:
            self.recordAuthentication = config["recordAuthentication"]
            if self.recordAuthentication is False:
                print(
                    "Starting Kable with recordAuthentication disabled, authentication requests will not be recorded")
        else:
            self.recordAuthentication = True

        self.queueFlushInterval = 10  # 10 seconds
        self.queueFlushTimer = None
        self.queueFlushMaxCount = 10  # 10 requests
        self.queueFlushMaxPoller = None
        self.queue = []

        self.validCache = TTLCache(maxsize=1000, ttl=30)
        self.invalidCache = TTLCache(maxsize=1000, ttl=30)

        self.kableEnvironment = "live" if self.environment == "live" else "test"

        url = f"{self.baseUrl}/api/authenticate"
        headers = {
            KABLE_ENVIRONMENT_HEADER_KEY: self.environment,
            KABLE_CLIENT_ID_HEADER_KEY: self.kableClientId,
            X_CLIENT_ID_HEADER_KEY: self.kableClientId,
            X_API_KEY_HEADER_KEY: self.kableClientSecret,
            KABLE_CLIENT_SECRET_HEADER_KEY: self.kableClientSecret,
        }

        try:
            response = requests.post(url=url, headers=headers)
            status = response.status_code
            if (status == 200):
                self.startFlushQueueOnTimer()
                self.startFlushQueueIfFullTimer()

                self.kill = False
                try:
                    signal.signal(signal.SIGINT, self.exitGracefully)
                    signal.signal(signal.SIGTERM, self.exitGracefully)
                except:
                    print("")

                print("Kable initialized successfully")

            elif status == 401:
                print("Failed to initialize Kable: Unauthorized")

            else:
                print(
                    f"Failed to initialize Kable: Something went wrong [{status}]")

        except Exception as e:
            print("Failed to initialize Kable: Something went wrong")

    def record(self, data):
        if (self.debug):
            print("Received data to record")

        clientId = None
        if 'clientId' in data:
            clientId = data['clientId']
            del data['clientId']

        customerId = None
        if 'customerId' in data:
            customerId = data['customerId']
            del data['customerId']

        self.enqueueEvent(clientId=clientId, customerId=customerId, data=data)


    def authenticate(self, api):
        @wraps(api)
        def decoratedApi(*args, **kwargs):
            if self.debug:
                print("Received request to authenticate")

            request = args[0]
            headers = request.headers

            clientId = headers[X_CLIENT_ID_HEADER_KEY] if X_CLIENT_ID_HEADER_KEY in headers else None
            secretKey = headers[X_API_KEY_HEADER_KEY] if X_API_KEY_HEADER_KEY in headers else None

            if self.environment is None or self.kableClientId is None:
                return JsonResponse({"message": "Unauthorized. Failed to initialize Kable: Configuration invalid"}, status=500)

            if clientId is None or secretKey is None:
                return JsonResponse({"message": "Unauthorized"}, status=401)

            if secretKey in self.validCache:
                if self.validCache[secretKey] == clientId:
                    if self.debug:
                        print("Valid Cache Hit")
                    if self.recordAuthentication:
                        self.enqueueEvent(clientId, None, {})
                    return api(*args)

            if secretKey in self.invalidCache:
                if self.invalidCache[secretKey] == clientId:
                    if self.debug:
                        print("Invalid Cache Hit")
                    return JsonResponse({"message": "Unauthorized"}, status=401)

            if self.debug:
                print("Authenticating at server")

            url = f"{self.baseUrl}/api/authenticate"
            headers = {
                KABLE_ENVIRONMENT_HEADER_KEY: self.environment,
                KABLE_CLIENT_ID_HEADER_KEY: self.kableClientId,
                X_CLIENT_ID_HEADER_KEY: clientId,
                X_API_KEY_HEADER_KEY: secretKey,
            }
            try:
                response = requests.post(url=url, headers=headers)
                status = response.status_code
                if (status == 200):
                    self.validCache.__setitem__(secretKey, clientId)
                    if self.recordAuthentication:
                        self.enqueueEvent(clientId, None, {})
                    return api(*args)
                else:
                    if status == 401:
                        self.invalidCache.__setitem__(secretKey, clientId)
                        return JsonResponse({"message": "Unauthorized"}, status=401)
                    else:
                        print("Unexpected " + status +
                              " response from Kable authenticate. Please update your SDK to the latest version immediately")
                        return JsonResponse({"message": "Something went wrong"}, status=500)

            except Exception as e:
                return JsonResponse({"message": "Something went wrong"}, status=500)

        return decoratedApi

    def enqueueEvent(self, clientId, customerId, data):
        event = {}
        event['environment'] = self.environment
        event['kableClientId'] = self.kableClientId
        event['clientId'] = clientId
        event['customerId'] = customerId
        event['timestamp'] = datetime.utcnow().isoformat()

        event['data'] = data

        library = {}
        library['name'] = 'kable-python-django'
        library['version'] = VERSION
        event['library'] = library

        self.queue.append(event)

    def flushQueue(self):
        if self.debug:
            print("Flushing Kable event queue...")

        if self.queueFlushTimer is not None:
            if self.debug:
                print('Stopping time-based queue poller')
            self.queueFlushTimer.cancel()
            self.queueFlushTimer = None

        if self.queueFlushMaxPoller is not None:
            if self.debug:
                print('Stopping size-based queue poller')
            self.queueFlushMaxPoller.cancel()
            self.queueFlushMaxPoller = None

        events = self.queue
        self.queue = []
        count = len(events)
        if (count > 0):
            if self.debug:
                print(f'Sending {count} batched events to server')

            url = f"{self.baseUrl}/api/events"
            headers = {
                KABLE_ENVIRONMENT_HEADER_KEY: self.environment,
                KABLE_CLIENT_ID_HEADER_KEY: self.kableClientId,
                X_CLIENT_ID_HEADER_KEY: self.kableClientId,
                X_API_KEY_HEADER_KEY: self.kableClientSecret
            }
            try:
                response = requests.post(
                    url=url, headers=headers, json=events)
                status = response.status_code
                if (status == 200):
                    print(
                        f'Successfully sent {count} events to Kable server')
                else:
                    print(f'Failed to send {count} events to Kable server')

            except Exception as e:
                print(f'Failed to send {count} events to Kable server')
        else:
            if self.debug:
                print('...no Kable events to flush...')

        if self.kill:
            sys.exit(0)
        else:
            self.startFlushQueueOnTimer()
            self.startFlushQueueIfFullTimer()

    def startFlushQueueOnTimer(self):
        if self.debug:
            print('Starting time-based queue poller')
        self.queueFlushTimer = Timer(
            self.queueFlushInterval, self.flushQueue).start()

    def startFlushQueueIfFullTimer(self):
        if self.debug:
            print('Starting size-based queue poller')
        self.queueMaxPoller = Timer(1, self.flushQueueIfFull).start()

    def flushQueueIfFull(self):
        events = self.queue
        if len(events) >= self.queueFlushMaxCount:
            self.flushQueue()

    def exitGracefully(self, *args):
        print(
            f'Kable will shut down gracefully within {self.queueFlushInterval} seconds')
        self.kill = True
        self.flushQueue()
