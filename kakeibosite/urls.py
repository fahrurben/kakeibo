"""
URL configuration for kakeibosite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from kakeibo.views.register_view import RegisterView
from kakeibo.views.expense_category_view import ExpenseCategoryView
from kakeibo.views.income_view import IncomeView
from kakeibo.views.expense_view import ExpenseView
from kakeibo.views.user_view import UserView

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'expense-categories', ExpenseCategoryView, 'expense-category')
router.register(r'incomes', IncomeView, 'income')
router.register(r'expenses', ExpenseView, 'expense')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/user/', UserView.as_view(), name='user'),

    path('api/', include(router.urls)),
]
