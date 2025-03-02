from django.db import models
from .custom_user import CustomUser
from .expense_category import ExpenseCategory


class Expense(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    details = models.CharField(max_length=1000)

    def __str__(self):
        return self.date.isoformat() + self.description
