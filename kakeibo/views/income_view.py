from rest_framework import viewsets

from ..models.income import Income
from ..serializers.income_serializer import IncomeSerializer
from ..permissions.user_owned_permission import UserOwnedPermission


class IncomeView(viewsets.ModelViewSet):
    serializer_class = IncomeSerializer
    permission_classes = [UserOwnedPermission]
    ordering_fields = ['date']
    ordering = ['date']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'user': self.request.user})
        return context

    def get_queryset(self):
        user = self.request.user
        month = self.request.query_params.get('month')
        year = self.request.query_params.get('year')

        query = Income.objects.filter(user=user)
        if month is not None and year is not None:
            query = query.filter(date__year__gte=year, date__month__gte=month,
                                 date__year__lte=year, date__month__lte=month)

        return query
