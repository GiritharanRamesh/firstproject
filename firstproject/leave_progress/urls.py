from django.urls import path
from .import views
urlpatterns = [
    path('LeaveProgressTable/', views.leave_info_tableApi)
]