from django.urls import path
from .import views
urlpatterns = [
    path('ExperienceTable/', views.experience_tableApi)
]