from rest_framework import serializers
from ..models.expense import Expense
from .expense_category_serializer import ExpenseCategorySerializer


class ExpenseSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField()
    category = ExpenseCategorySerializer(read_only=True)

    class Meta:
        model = Expense
        fields = ('id', 'category_id', 'category', 'date', 'description',
                  'amount', 'details', 'created_at', 'updated_at', )

    def create(self, validated_data):
        current_user = self.context['user']
        return Expense.objects.create(**validated_data, user=current_user)

    def update(self, instance, validated_data):
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.date = validated_data.get('date', instance.date)
        instance.description = validated_data.get('description', instance.description)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.details = validated_data.get('details', instance.details)
        instance.save()
        return instance
