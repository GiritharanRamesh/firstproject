from django.urls import path
from .import views
urlpatterns = [
    path('SkillsTable/', views.skills_tableApi)
]