from django.urls import path
from .import views
urlpatterns = [
    path('JobInfoTable/', views.job_info_tableApi)
]