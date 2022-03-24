from django.urls import path
from .import views
urlpatterns = [
    path('CompensationTable/', views.compensationinfo_tableApi),
]