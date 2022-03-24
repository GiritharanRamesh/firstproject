from django.urls import path
from .import views
urlpatterns = [
    path('PersonalInfoTable/', views.personal_info_tableApi)
]