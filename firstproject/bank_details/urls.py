from django.urls import path
from .import views
urlpatterns = [
    path('BankDetailsTable/', views.bankdetails_tableApi),
]