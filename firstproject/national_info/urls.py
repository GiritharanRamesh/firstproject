from django.urls import path
from .import views
urlpatterns = [
    path('NationalInfoTable/', views.national_info_tableApi)
]