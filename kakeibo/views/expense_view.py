from rest_framework import viewsets

from ..models.expense import Expense
from ..serializers.expense_serializer import ExpenseSerializer
from ..permissions.user_owned_permission import UserOwnedPermission


class ExpenseView(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [UserOwnedPermission]
    ordering_fields = ['date', 'category']
    ordering = ['date']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'user': self.request.user})
        return context

    def get_queryset(self):
        user = self.request.user
        month = self.request.query_params.get('month')
        year = self.request.query_params.get('year')

        query = Expense.objects.filter(user=user)
        if month is not None and year is not None:
            query = query.filter(date__year__gte=year, date__month__gte=month,
                                 date__year__lte=year, date__month__lte=month)

        return query
