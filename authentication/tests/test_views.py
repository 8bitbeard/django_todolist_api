from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from todos.models import Todo


class AuthAPITestCase(APITestCase):

    def authenticate(self):
        self.client.post(reverse('register'), { 'username': 'username', 'email': 'email@email.com', 'password': 'password'})
        response = self.client.post(reverse('login'), { 'email': 'email@email.com', 'password': 'password' })
        self.client.credentials (HTTP_AUTHORIZATION = "Bearer {}".format(response.data['token']))


class RegisterAPIView(AuthAPITestCase):

    def test_should_register_a_new_user(self):
        response = self.client.post(reverse('register'), { 'username': 'Will', 'email': 'will@example.com', 'password': 'will1234' })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], 'Will')
        self.assertEqual(response.data['email'], 'will@example.com')


# class AuthUserAPIView(AuthAPITestCase):
