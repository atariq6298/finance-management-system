from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
from django.contrib import admin
router = DefaultRouter()
router.register(r'transactions', views.TransactionViewSet, basename='transaction')
router.register(r'budgets', views.BudgetViewSet, basename='budget')
router.register(r'accounts', views.AccountViewSet, basename='account')
router.register(r'recurring-expenses', views.RecurringExpenseViewSet, basename='recurring-expense')
router.register(r'recurring-incomes', views.RecurringIncomeViewSet, basename='recurring-income')
router.register(r'incomes', views.IncomeViewSet, basename='income')
router.register(r'expenses', views.ExpenseViewSet, basename='expense')
urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls)
]