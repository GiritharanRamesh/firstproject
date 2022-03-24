from django.urls import path
from .import views
urlpatterns = [
    path('ProspectCandidate/', views.prospectcandidate_Api)
]