from typing import Dict, Optional, Union

from rhino_health.lib.constants import ApiEnvironment
from rhino_health.lib.rest_api.api_request import APIRequest
from rhino_health.lib.rest_api.api_response import APIResponse
from rhino_health.lib.rest_api.request_adapter import RequestAdapter

RequestDataType = Union[str, dict, list]
AdapterTableType = Dict[str, RequestAdapter]


class RestHandler:
    def __init__(
        self,
        session,
        base_url: str = ApiEnvironment.LOCALHOST_API_URL,
        adapters: AdapterTableType = None,
    ):
        self.session = session
        self.adapters: AdapterTableType = adapters
        self.base_url = base_url

    def get(
        self, url: str, params: Optional[dict] = None, adapter_kwargs: Optional[dict] = None
    ) -> APIResponse:
        return self._make_request(
            method="get",
            base_url=self.base_url,
            url=url,
            params=params,
            data=None,
            adapter_kwargs=adapter_kwargs,
        )

    # Note the ordering is different from get as data is more often used in post requests.
    def post(
        self,
        url: str,
        data: RequestDataType,
        params: Optional[dict] = None,
        adapter_kwargs: Optional[dict] = None,
    ) -> APIResponse:
        return self._make_request(
            method="post",
            base_url=self.base_url,
            url=url,
            params=params,
            data=data,
            adapter_kwargs=adapter_kwargs,
        )

    # def _ensure_json(self, payload: Union[str, dict, list]) -> str:
    #     if isinstance(payload, (dict, list)):
    #         return json.dumps(payload)
    #     return payload

    def _make_request(
        self,
        method: str,
        base_url: str,
        url: str,
        params: Optional[dict],
        data: Optional[RequestDataType],
        adapter_kwargs: Optional[dict],
    ) -> APIResponse:
        # TODO: Automatic retry and backoff
        request = APIRequest(
            session=self.session,
            method=method,
            base_url=base_url,
            url=url,
            params=params,
            data=data,
        )
        adapter_kwargs = adapter_kwargs or {}
        response = None
        # TODO: Max request count prevent endless loops
        while request.pending:
            for adapter in self.adapters.values():
                adapter.before_request(request, adapter_kwargs)
            request.request_status = APIRequest.RequestStatus.PENDING
            response = request.make_request()
            for adapter in self.adapters.values():
                adapter.after_request(request, response, adapter_kwargs)
        return response
