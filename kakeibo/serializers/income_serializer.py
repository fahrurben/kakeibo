from rest_framework import serializers
from ..models.income import Income


class IncomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Income
        fields = ('id', 'date', 'description', 'amount', 'created_at', 'updated_at', )

    def create(self, validated_data):
        current_user = self.context['user']
        return Income.objects.create(**validated_data, user=current_user)

    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.description = validated_data.get('description', instance.description)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.save()
        return instance
