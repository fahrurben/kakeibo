from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.views import status
import datetime
from kakeibo.models.custom_user import CustomUser
from kakeibo.models.income import Income


class IncomeTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user1 = CustomUser.create(
            'user1',
            'test1@test.com',
            'secret123',
            datetime.datetime(1990, 1, 1)
        )
        cls.income1 = Income.objects.create(
            user=cls.user1,
            date=datetime.datetime(2025, 1, 1),
            description='Salary',
            amount=1000000
        )

    def test_create(self):
        self.client.force_authenticate(self.user1)
        url = reverse('income-list')
        response = self.client.post(url, {
            'date': '2025-01-01',
            'description': 'Lorem ipsum',
            'amount': 1000
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get(self):
        self.client.force_authenticate(self.user1)
        url = reverse('income-detail', args=[self.income1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.post(url, {
            'date': '2025-01-01',
            'description': 'Lorem ipsum',
            'amount': 1000
        })

    def test_update(self):
        self.client.force_authenticate(self.user1)
        url = reverse('income-detail', args=[self.income1.id])
        response = self.client.patch(url, {
            'description': 'Lorem ipsum updated',
            'amount': 2000
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.put(url, {
            'description': 'Lorem ipsum updated',
            'amount': 2000
        })

    def test_delete(self):
        self.client.force_authenticate(self.user1)
        url = reverse('income-detail', args=[self.income1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
