from django.urls import path
from .import views
urlpatterns = [
    path('ManagementInfoTable/', views.management_info_tableApi)
]