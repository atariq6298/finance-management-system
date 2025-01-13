from django.test import TestCase
from .models import YourModel, Expense, Income, Budget, Account, Transaction, RecurringExpense, RecurringIncome  # Replace with your actual model

class YourModelTests(TestCase):
    def setUp(self):
        # Set up any initial data for your tests here
        YourModel.objects.create(field1='value1', field2='value2')  # Replace with actual fields

    def test_model_creation(self):
        """Test that the model is created correctly."""
        obj = YourModel.objects.get(field1='value1')
        self.assertEqual(obj.field2, 'value2')  # Replace with actual assertions

    def test_model_str(self):
        """Test the string representation of the model."""
        obj = YourModel.objects.get(field1='value1')
        self.assertEqual(str(obj), 'Expected String Representation')  # Replace with actual expected value

class ExpenseModelTest(TestCase):
    def setUp(self):
        self.expense = Expense.objects.create(
            name="Test Expense",
            amount=100.00,
            date="2023-10-01",
            category="Test Category",
            currency="USD",
            notes="Test notes",
            tags="test,expense"
        )

    def test_expense_creation(self):
        self.assertEqual(self.expense.name, "Test Expense")
        self.assertEqual(self.expense.amount, 100.00)
    
    def tearDown(self):
        self.expense.delete()

class IncomeModelTest(TestCase):
    def setUp(self):
        self.income = Income.objects.create(
            source="Test Source",
            amount=200.00,
            date="2023-10-01",
            currency="USD",
            notes="Test notes",
            tags="test,income"
        )

    def test_income_creation(self):
        self.assertEqual(self.income.source, "Test Source")
        self.assertEqual(self.income.amount, 200.00)

    def tearDown(self):
        self.income.delete()

class BudgetModelTest(TestCase):
    def setUp(self):
        self.budget = Budget.objects.create(
            name="Test Budget",
            total_amount=1000.00,
            from_date="2023-10-01",
            to_date="2023-12-31",
            is_active=True
        )

    def test_budget_creation(self):
        self.assertEqual(self.budget.name, "Test Budget")
        self.assertEqual(self.budget.total_amount, 1000.00)
    def tearDown(self):
        self.budget.delete()

class AccountModelTest(TestCase):
    def setUp(self):
        self.account = Account.objects.create(
            name="Test Account",
            balance=5000.00,
            account_type="Checking"
        )

    def test_account_creation(self):
        self.assertEqual(self.account.name, "Test Account")
        self.assertEqual(self.account.balance, 5000.00)
    def tearDown(self):
        self.account.delete()   
        
class TransactionModelTest(TestCase):
    def setUp(self):
        self.budget = Budget.objects.create(
            name="Test Budget",
            total_amount=1000.00,
            from_date="2023-10-01",
            to_date="2023-12-31",
            is_active=True
        )
        self.account = Account.objects.create(
            name="Test Account",
            balance=5000.00,
            account_type="Checking"
        )
        self.transaction = Transaction.objects.create(
            budget=self.budget,
            description="Test Transaction",
            amount=100.00,
            transaction_date="2023-10-01T12:00:00Z",
            currency="USD",
            notes="Test notes",
            tags="test,transaction",
            account=self.account
        )

    def test_transaction_creation(self):
        self.assertEqual(self.transaction.description, "Test Transaction")
        self.assertEqual(self.transaction.amount, 100.00)
    def tearDown(self):
        self.transaction.delete()
        self.budget.delete()
        self.account.delete()

class RecurringExpenseModelTest(TestCase):
    def setUp(self):
        self.recurring_expense = RecurringExpense.objects.create(
            name="Test Recurring Expense",
            amount=50.00,
            start_date="2023-10-01",
            frequency="Monthly",
            category="Test Category",
            currency="USD",
            notes="Test notes",
            tags="test,recurring"
        )

    def test_recurring_expense_creation(self):
        self.assertEqual(self.recurring_expense.name, "Test Recurring Expense")
        self.assertEqual(self.recurring_expense.amount, 50.00)

    def tearDown(self):
        self.recurring_expense.delete()


class RecurringIncomeModelTest(TestCase):
    def setUp(self):
        self.recurring_income = RecurringIncome.objects.create(
            source="Test Recurring Income",
            amount=150.00,
            start_date="2023-10-01",
            frequency="Monthly",
            currency="USD",
            notes="Test notes",
            tags="test,recurring"
        )

    def test_recurring_income_creation(self):
        self.assertEqual(self.recurring_income.source, "Test Recurring Income")
        self.assertEqual(self.recurring_income.amount, 150.00)

    def tearDown(self): 
        self.recurring_income.delete()
        