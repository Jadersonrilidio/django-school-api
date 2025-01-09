from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class AuthenticationUserTestCase(APITestCase):
    fixtures = ['db_prototype.json']

    def setUp(self):
        # {"pk": 1, "password": "pbkdf2_sha256$870000$Nk6nKZVQL2NSdTPumz6CWl$cIWPtP1iE43+faaNsxNNBqKemM+dRMlIwOvTEKaiBr0=", "last_login": "2024-12-06T13:52:13.489Z", "is_superuser": true, "username": "jay", "first_name": "", "last_name": "", "email": "jay@gmail.com", "is_staff": true, "is_active": true, "date_joined": "2024-11-26T22:59:44.098Z", "groups": [], "user_permissions": []}
        self.user = User.objects.get(username='jay')
        self.url = reverse('Students-list')

    def test_user_can_authenticate_given_correct_credential(self):
        """Test to verify user authentication provided correct credentials"""
        user = authenticate(request=None, username="jay", password="admin123")
        self.assertTrue(user is not None and user.is_authenticated)
        self.assertEqual(user, self.user)

    def test_user_cannot_authenticate_given_incorrect_username(self):
        """Test to verify user authentication fails provided incorrect username credential"""
        user = authenticate(request=None, username="anotherjay", password="admin123")
        self.assertTrue(user is None)

    def test_user_cannot_authenticate_given_incorrect_password(self):
        """Test to verify user authentication fails provided incorrect password credential"""
        user = authenticate(request=None, username="jay", password="anotheradmin123")
        self.assertTrue(user is None)

    def test_get_request_authorized(self):
        """Test verifies if GET request is authorized"""
        self.client.force_authenticate(self.user)
        response = self.client.get(path=self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_request_unauthorized(self):
        """Test verifies if GET request is unauthorized"""
        response = self.client.get(path=self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)