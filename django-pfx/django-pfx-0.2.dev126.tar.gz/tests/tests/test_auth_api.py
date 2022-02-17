import logging
import re
from datetime import datetime, timedelta
from http.cookies import SimpleCookie

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core import mail
from django.test import TransactionTestCase, override_settings
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

import jwt

from pfx.pfxcore.test import APIClient, TestAssertMixin

logger = logging.getLogger(__name__)


class AuthAPITest(TestAssertMixin, TransactionTestCase):

    def setUp(self):
        self.client = APIClient(default_locale='en')
        self.cookie_client = APIClient(default_locale='en', with_cookie=True)
        self.user1 = User.objects.create_user(
            username='jrr.tolkien',
            email="jrr.tolkien@oxford.com",
            password='RIGHT PASSWORD',
            first_name='John Ronald Reuel',
            last_name='Tolkien',
        )

    def test_invalid_login(self):
        response = self.client.post(
            '/api/auth/login', {
                'username': 'jrr.tolkien',
                'password': 'WRONG PASSWORD'})
        self.assertRC(response, 401)

    def test_valid_login(self):
        response = self.client.post(
            '/api/auth/login', {
                'username': 'jrr.tolkien',
                'password': 'RIGHT PASSWORD'})

        self.assertRC(response, 200)
        decoded = jwt.decode(
            response.json_content['token'], settings.PFX_SECRET_KEY,
            algorithms="HS256")
        self.assertEqual(decoded['pfx_user_pk'], self.user1.pk)

    def test_valid_login_with_cookie(self):
        response = self.client.post(
            '/api/auth/login?mode=cookie', {
                'username': 'jrr.tolkien',
                'password': 'RIGHT PASSWORD'})

        cookie = [v for k, v in response.client.cookies.items()
                  if k == 'token'][0]
        regex = r".*token=([\w\._-]*);.*"
        token = re.findall(regex, str(cookie))[0]

        self.assertRC(response, 200)
        decoded = jwt.decode(
            token, settings.PFX_SECRET_KEY,
            algorithms="HS256")
        self.assertEqual(decoded['pfx_user_pk'], self.user1.pk)

    def test_valid_change_password(self):
        self.client.login(
                username='jrr.tolkien',
                password='RIGHT PASSWORD')
        response = self.client.post(
            '/api/auth/change-password', {
                'old_password': 'RIGHT PASSWORD',
                'new_password': 'NEW RIGHT PASSWORD'})
        self.assertRC(response, 200)

        self.cookie_client.login(
                username='jrr.tolkien',
                password='RIGHT PASSWORD')
        response = self.client.post(
            '/api/auth/change-password', {
                'old_password': 'NEW RIGHT PASSWORD',
                'new_password': 'RIGHT PASSWORD'})
        self.assertRC(response, 200)

    def test_invalid_change_password(self):
        self.client.login(
                username='jrr.tolkien',
                password='RIGHT PASSWORD')
        response = self.client.post(
            '/api/auth/change-password', {
                'old_password': 'WRONG PASSWORD',
                'new_password': 'NEW RIGHT PASSWORD'})
        self.assertRC(response, 401)

    @override_settings(PFX_TOKEN_VALIDITY={'minutes': 30})
    def test_valid_token_with_expiration(self):
        self.client.login(
                username='jrr.tolkien',
                password='RIGHT PASSWORD')
        response = self.client.get(
            '/api/books')
        self.assertRC(response, 200)

    @override_settings(PFX_TOKEN_VALIDITY={'minutes': 30})
    def test_valid_cookie_token_with_expiration(self):
        self.cookie_client.login(
                username='jrr.tolkien',
                password='RIGHT PASSWORD')

        regex = r".*expires=([^;]*);.*"
        expires = re.findall(regex, str(self.cookie_client.auth_cookie))[0]
        d = datetime.strptime(expires, '%a, %d %b %Y %H:%M:%S %Z')

        regex = r".*Max-Age=([^;]*);.*"
        max_age = re.findall(regex, str(self.cookie_client.auth_cookie))[0]

        # cookie expires in 30 minutes +/- 5 minutes.
        self.assertTrue(
            datetime.utcnow() + timedelta(minutes=25) <
            d < datetime.utcnow() + timedelta(minutes=35))
        self.assertEqual(int(max_age), 1800)

        response = self.cookie_client.get(
            '/api/books')
        self.assertRC(response, 200)

    @override_settings(PFX_TOKEN_VALIDITY={'minutes': -30})
    def test_expired_token(self):
        self.client.login(
                username='jrr.tolkien',
                password='RIGHT PASSWORD')

        response = self.client.get(
            '/api/books')
        self.assertRC(response, 401)

    @override_settings(PFX_TOKEN_VALIDITY={'minutes': -30})
    def test_expired_cookie_token(self):
        self.cookie_client.login(
                username='jrr.tolkien',
                password='RIGHT PASSWORD')

        regex = r".*expires=([^;]*);.*"
        expires = re.findall(regex, str(self.cookie_client.auth_cookie))[0]
        d = datetime.strptime(expires, '%a, %d %b %Y %H:%M:%S %Z')

        regex = r".*Max-Age=([^;]*);.*"
        max_age = re.findall(regex, str(self.cookie_client.auth_cookie))[0]

        # cookie expires now +/- 5 minutes.
        self.assertTrue(
            datetime.utcnow() - timedelta(minutes=5) <
            d < datetime.utcnow() + timedelta(minutes=5))
        self.assertEqual(int(max_age), 0)

        response = self.cookie_client.get(
            '/api/books')
        self.assertRC(response, 401)

    def test_invalid_token(self):
        token = jwt.encode(
            {'pfx_user_pk': 1}, "A WRONG SECRET", algorithm="HS256")
        logging.disable(logging.CRITICAL)
        response = self.client.get(
            '/api/books',
            HTTP_AUTHORIZATION='Bearer ' + token,
            content_type='application/json')
        logging.disable(logging.NOTSET)
        self.assertRC(response, 401)

    def test_invalid_cookie_token(self):
        token = jwt.encode(
            {'pfx_user_pk': 1}, "A WRONG SECRET", algorithm="HS256")
        logging.disable(logging.CRITICAL)
        self.client.cookies = SimpleCookie({'token': token})
        response = self.client.get(
            '/api/books',
            content_type='application/json')
        logging.disable(logging.NOTSET)
        self.assertRC(response, 401)

    def test_signup(self):
        # Try to create with an existing username
        response = self.client.post(
            '/api/auth/signup', {
                'username': 'jrr.tolkien',
                'email': "jrr.tolkien@oxford.com",
                'first_name': 'John Ronald Reuel',
                'last_name': 'Tolkien',
            })

        self.assertRC(response, 422)
        self.assertEqual(response.json_content['username'],
                         ['A user with that username already exists.'])

        # Then create another valid user
        response = self.client.post(
            '/api/auth/signup', {
                'username': 'isaac.asimov',
                'email': 'isaac.asimov@bu.edu',
                'first_name': 'Isaac',
                'last_name': 'Asimov',
            })

        self.assertRC(response, 200)

        # Must send a welcome email
        self.assertEqual(
            mail.outbox[0].subject,
            f'Welcome on {settings.PFX_SITE_NAME}')

        self.client.logout()

        # Test that the token and uid are valid.
        regex = r"token=(.*)&uidb64=(.*)"
        token, uidb64 = re.findall(regex, mail.outbox[0].body)[0]
        response = self.client.post(
            '/api/auth/set-password', {
                'token': token,
                'uidb64': uidb64,
                'password': 'test',
                'check_password': 'test'
            })
        self.assertRC(response, 200)
        self.assertJE(response, 'message', 'password updated successfully')

    def test_forgotten_password(self):
        # Try with an nonexistent email
        response = self.client.post(
            '/api/auth/forgotten-password', {
                'email': 'isaac.asimov@bu.edu',
            })

        self.assertRC(response, 404)

        # Then try with a valid email
        response = self.client.post(
            '/api/auth/forgotten-password', {
                'email': 'jrr.tolkien@oxford.com',
            })

        self.assertRC(response, 200)

        # Must send a reset password email
        self.assertEqual(
            mail.outbox[0].subject,
            f'Password reset on {settings.PFX_SITE_NAME}')

        self.client.logout()

        # Test that the token and uid are valid.
        regex = r"token=(.*)&uidb64=(.*)"
        token, uidb64 = re.findall(regex, mail.outbox[0].body)[0]
        response = self.client.post(
            '/api/auth/set-password', {
                'token': token,
                'uidb64': uidb64,
                'password': 'test',
                'check_password': 'test'
            })
        self.assertRC(response, 200)
        self.assertJE(response, 'message', 'password updated successfully')

    def test_set_password(self):
        # Try with a wrong token and uid
        response = self.client.post(
            '/api/auth/set-password', {
                'token': 'WRONG TOKEN',
                'uidb64': 'WRONG UID',
                'password': 'NEW PASSWORD',
            })

        self.assertRC(response, 401)

        # Then try with a valid token and uid
        token = default_token_generator.make_token(self.user1)
        uid = urlsafe_base64_encode(force_bytes(self.user1.pk))
        response = self.client.post(
            '/api/auth/set-password', {
                'token': token,
                'uidb64': uid,
                'password': 'NEW PASSWORD',
            })
        self.assertRC(response, 200)
