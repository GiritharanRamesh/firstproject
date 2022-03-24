from django.urls import path
from .import views
urlpatterns = [
    path('ContactTable/', views.contact_tableApi)
]