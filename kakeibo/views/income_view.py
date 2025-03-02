from rest_framework import viewsets

from ..models.income import Income
from ..serializers.income_serializer import IncomeSerializer
from ..permissions.user_owned_permission import UserOwnedPermission


class IncomeView(viewsets.ModelViewSet):
    serializer_class = IncomeSerializer
    permission_classes = [UserOwnedPermission]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'user': self.request.user})
        return context

    def get_queryset(self):
        user = self.request.user
        return Income.objects.filter(user=user)
