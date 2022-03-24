from django.urls import path
from .import views
urlpatterns = [
    path('TimeSheetInfoTable/', views.time_sheet_tableApi)
]