from rest_framework import viewsets
from .models import Transaction, Budget
from .serializers import TransactionSerializer, BudgetSerializer
from .models import Account, RecurringExpense, RecurringIncome, Expense, Income
from .serializers import AccountSerializer, RecurringExpenseSerializer, RecurringIncomeSerializer, ExpenseSerializer, IncomeSerializer
class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class RecurringExpenseViewSet(viewsets.ModelViewSet):
    queryset = RecurringExpense.objects.all()
    serializer_class = RecurringExpenseSerializer

class RecurringIncomeViewSet(viewsets.ModelViewSet):
    queryset = RecurringIncome.objects.all()
    serializer_class = RecurringIncomeSerializer


