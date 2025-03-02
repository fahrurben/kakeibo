from rest_framework import viewsets

from ..models.expense_category import ExpenseCategory
from ..serializers.expense_category_serializer import ExpenseCategorySerializer
from ..permissions.user_owned_permission import UserOwnedPermission

class ExpenseCategoryView(viewsets.ModelViewSet):
    serializer_class = ExpenseCategorySerializer
    permission_classes = [UserOwnedPermission]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'user': self.request.user})
        return context

    def get_queryset(self):
        user = self.request.user
        return ExpenseCategory.objects.filter(user=user)