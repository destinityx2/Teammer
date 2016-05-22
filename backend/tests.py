    # This file is part of Teammer.

    # Teammer is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, version 3.

    # Teammer is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with Teammer.  If not, see <http://www.gnu.org/licenses/>.

from django.test import TestCase

# Create your tests here.

from django.test import Client

from backend.models import User
from backend.models import UserInfo
from backend.models import ProjectUsers
from backend.models import Applicants

from backend.views import *

"""
Testing using the Test Client
The test client is a class that can act like a simple
browser for testing purposes.

It allows the user to compose GET and POST requests, and
obtain the response that the server gave to those requests.
The server Response objects are annotated with the details
of the contexts and templates that were rendered during the
process of serving the request.

``Client`` objects are stateful - they will retain cookie (and
thus session) details for the lifetime of the ``Client`` instance.
"""


class UnitTestCase(TestCase):
    """ Testing basic user creation / foreign key creation
    """
    def setUp(self):
        user = User.objects.create_user('Tester', 'some@somewhere.com', 'qwerty')

    def test_users_are_creatable(self):
        """ Testing if users that we just tried to create is stated in DB
            and we can also find this user by any field (except password)
        """
        user = User.objects.get(username="Tester")
        self.assertNotEqual(user, None)

        user = User.objects.get(email="some@somewhere.com")
        self.assertNotEqual(user, None)

    def test_users_are_linked(self):
        """ Testing if we can find user from any table that is linked to User table
            for example, UserInfo
        """
        user = User.objects.get(username="Tester")
        UserInfo.objects.create(user=user)

        user_info = UserInfo.objects.get(user=user)
        self.assertNotEqual(user_info, None)

        linked_user = user_info.user
        self.assertEqual(user, linked_user)


class BrowserTestCase(TestCase):
    """ Testing different browser interactions
    """
    def setUp(self):
        pass

    def test_check_main_page_response(self):
        """ Testing if we don't get 404 code in Mozilla or Opera like browsers
        """
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
    """ Testing response codes for different browsers
    """
    def setUp(self):
        pass

    def test_if_main_page_allows_login(self):
        """ Testing if user is not logged in then "Sign In" button is present for them
        """
        some_client = Client()
        response = some_client.get('/index')

        self.assertNotEqual(response.status_code, 404)

    def test_if_login_changes_content(self):
        """ Testing if user that is logged in now can see "Logout" button
        """
        user = User.objects.create_user('Tester', 'some@somewhere.com', 'qwerty')
        some_client = Client()
        some_client.force_login(user)

        response = some_client.get('/index')

        self.assertNotEqual(response.status_code, 404)

        if response.status_code == 200:
            self.assertContains(response, "Logout")


class ClientInterationTestCase(TestCase):
    """ Testing client interaction with web-site such as incorrect urls
    """
    def setUp(self):
        pass

    def test_unknown_page(self):
        """ Testing if user will get consistent code in case he'll try to access
            page that does not exist
        """
        u1 = User.objects.create_user(username='testclient', password='password')

        client = Client()
        client.force_login(u1)
        response = client.get('/some_non_existing_link')
        self.assertEqual(response.status_code, 404)

    def test_view_with_bad_login(self):
        """ Testing if user with credentials is not going to log in
        """
        client = Client()
        login = client.login(username='otherusername', password='nopassword')

        self.assertFalse(login)


class RenderToResponseTestCase(TestCase):
    """ Testing what happens with client after he simply visits the page
    """
    def test_index_with_response(self):
        """ Testing login view and redirection that happens
            after interacting with it
        """
        response = self.client.get('/index/')

        self.assertContains(response, "Home")
        self.assertEqual(response.status_code, 200)

    def test_about_with_response(self):
        """ Testing about view and it's return value
        """

        response = self.client.get('/index/about/')
        self.assertContains(response, "About")
        self.assertEqual(response.status_code, 200)

    def test_projects_with_response(self):
        """ Testing projects page for it's return value
        """

        response = self.client.get('/index/projects/')
        self.assertContains(response, "Projects")
        self.assertEqual(response.status_code, 200)

    def test_notfound_response(self):
        """ Check if Non-existing pages giving 404 http code
        """
        response = self.client.get('/bad_view/')

        self.assertEqual(response.status_code, 404)

    def test_post_register_project(self):
        """ Check if we gettin redirected after posting
            registration request
        """
        u1 = User.objects.create_user(username='testclient', password='password')
        client = Client()
        client.force_login(u1)

        post_data = {'project_name':'Something',
                     'description':'Test',
                     'skills':'Test',
                     'num_members':5}

        response = client.post('/index/register_project/', post_data, follow=True)

        self.assertNotEqual(response.status_code, 404)
