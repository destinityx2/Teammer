from django.test import TestCase

# Create your tests here.

from django.test import Client

from backend.models import User
from backend.models import UserInfo
from backend.models import ProjectUsers
from backend.models import Applicants


class UnitTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('Tester', 'some@somewhere.com', 'qwerty')

    def test_users_are_creatable(self):
        user = User.objects.get(username="Tester")
        self.assertNotEqual(user, None)

        user = User.objects.get(email="some@somewhere.com")
        self.assertNotEqual(user, None)

    def test_users_are_linked(self):
        user = User.objects.get(username="Tester")
        UserInfo.objects.create(user=user)

        user_info = UserInfo.objects.get(user=user)
        self.assertNotEqual(user_info, None)

        linked_user = user_info.user
        self.assertEqual(user, linked_user)


class BrowserTestCase(TestCase):
    def setUp(self):
        pass

    def test_check_main_page_response(self):
        c_mozilla = Client(HTTP_USER_AGENT='Mozilla/5.0')
        c_opera_9 = Client(HTTP_USER_AGENT='Opera/9.80')
        c_opera_12 = Client(HTTP_USER_AGENT='Opera/12.0')

        response_mozilla = c_mozilla.get('/index')
        response_opera_9 = c_opera_9.get('/index')
        response_opera_12 = c_opera_12.get('/index')

        self.assertNotEqual(response_mozilla.status_code, 404)
        self.assertNotEqual(response_opera_9.status_code, 404)
        self.assertNotEqual(response_opera_12.status_code, 404)


class UserBehaviorTestCase(TestCase):
    def setUp(self):
        pass

    def test_if_main_page_allows_login(self):
        some_client = Client()
        response = some_client.get('/index')

        self.assertContains(response, "Sign in")

    def test_if_login_changes_content(self):
        user = User.objects.get(pk=1)
        some_client = Client(user=user)
        some_client.force_login()

        response = some_client.get('/index')

        self.assertNotEqual(response.status_code, 404)

        if response.status_code == 200:
            self.assertContains(response., "Logout")