from django.db import models
from .custom_user import CustomUser


class ExpenseCategory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Types(models.TextChoices):
        ESSENTIAL = 'ES', 'Essential'
        OPTIONAL = 'OP', 'Optional'
        ENTERTAINMENT = 'EN', 'Entertainment'
        EXTRA = 'EX', 'Extra'

    type = models.CharField(max_length=2, choices=Types.choices)
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user_id', 'name'], name='unique_expense_category_name')
        ]

    def __str__(self):
        return self.name
