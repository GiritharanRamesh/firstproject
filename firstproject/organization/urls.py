from django.urls import path
from .import views
urlpatterns = [
    path('OrganizationTable/', views.organization_tableApi)
]