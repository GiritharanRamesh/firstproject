from django.urls import path
from .import views
urlpatterns = [
    path('Employee1/', views.employee_Api),
    path('CompensationInfo/', views.compensationinfo_Api),
    path('Contact1/', views.contact_Api),
    path('EmergencyContact/', views.emergency_Api),
    path('Experience1/', views.experience_Api),
    path('JobInfo/', views.jobinfo_Api),
    path('LeaveInfo/', views.leaveinfo_Api),
    path('ManagementInfo/', views.managementinfo_Api),
    path('NationalInfo/', views.nationalinfo_Api),
    path('Organization1/', views.organization_Api),
    path('PersonalInfo/', views.personalinfo_Api),
    path('Qualification1/', views.qualification_Api),
    path('Skills1/', views.skills_Api),
    path('TimeSheetInfo/', views.timesheet_Api),
    path('BankDetails/', views.bankdetails_Api)
]