from django.urls import path
from .import views
urlpatterns = [
    path('QualificationTable/', views.qualification_tableApi)
]