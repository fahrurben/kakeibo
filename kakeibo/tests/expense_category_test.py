from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.views import status
import datetime
from kakeibo.models.custom_user import CustomUser
from kakeibo.models.expense_category import ExpenseCategory

class ExpenseCategoryTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user1 = CustomUser.create(
            'user1',
            'test1@test.com',
            'secret123',
            datetime.datetime(1990, 1, 1)
        )
        cls.expense_category1 = ExpenseCategory.objects.create(
            user=cls.user1,
            type=ExpenseCategory.Types.ESSENTIAL,
            name='Test',
            description='Lorem ipsum',
            is_active=True
        )

    def test_create(self):
        self.client.force_authenticate(self.user1)
        url = reverse('expense-category-list')
        response = self.client.post(url, {
            'type': 'ES',
            'name': 'Test2',
            'description': 'Lorem ipsum',
            'is_active': True,
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get(self):
        self.client.force_authenticate(self.user1)
        url = reverse('expense-category-detail', args=[self.expense_category1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.post(url, {
            'type': 'ES',
            'name': 'Test',
            'description': 'Lorem ipsum',
            'is_active': True,
        })

    def test_update(self):
        self.client.force_authenticate(self.user1)
        url = reverse('expense-category-detail', args=[self.expense_category1.id])
        response = self.client.patch(url, {
            'type': 'ES',
            'name': 'Test Updated',
            'description': 'Lorem ipsum',
            'is_active': True,
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.put(url, {
            'type': 'ES',
            'name': 'Test Updated',
            'description': 'Lorem ipsum',
            'is_active': True,
        })

    def test_delete(self):
        self.client.force_authenticate(self.user1)
        url = reverse('expense-category-detail', args=[self.expense_category1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)