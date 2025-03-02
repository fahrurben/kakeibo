from rest_framework import serializers
from ..models.expense_category import ExpenseCategory


class ExpenseCategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ExpenseCategory
        fields = ('id', 'type', 'name', 'description', 'is_active', 'created_at', 'updated_at', )

    def validate_name(self, value):
        current_user = self.context['user']
        if self.instance:
            is_exist = ExpenseCategory.objects.filter(user=current_user, name=value).exclude(id=self.instance.id).exists()
        else:
            is_exist = ExpenseCategory.objects.filter(user=current_user, name=value).exists()

        if is_exist:
            raise serializers.ValidationError("Name already exists")
        return value

    def create(self, validated_data):
        current_user = self.context['user']
        return ExpenseCategory.objects.create(**validated_data, user=current_user)

    def update(self, instance, validated_data):
        instance.type = validated_data.get('type', instance.type)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance
