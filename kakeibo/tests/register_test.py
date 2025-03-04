from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.views import status


class RegisterTest(APITestCase):

    def test_register(self):
        url = reverse('register')
        response = self.client.post(url, {
            'email': 'test1@test.com',
            'username': 'user1',
            'password': 'secret123',
            'birthday': '1990-01-01'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'email': 'test1@test.com',
            'username': 'user1',
            'birthday': '1990-01-01'
        })
