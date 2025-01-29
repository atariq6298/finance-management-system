from django.contrib import admin
from .models import Expense, Income, Budget, Transaction, RecurringExpense, RecurringIncome  # Import actual model names

admin.site.register(Expense)  # Register Expense model
admin.site.register(Income)  # Register Income model
admin.site.register(Budget)  # Register Budget model
admin.site.register(Transaction)  # Register Transaction model
admin.site.register(RecurringExpense)  # Register RecurringExpense model
admin.site.register(RecurringIncome)  # Register RecurringIncome model