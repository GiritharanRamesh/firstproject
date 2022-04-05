from rest_framework import viewsets
from .models import Compensationinfo, Employee1, Contact1, Emergencycontact, Experience1, Jobinfo, Leaveinfo, Managementinfo, Nationalinfo, Organization1, Personalinfo, Qualification1, Skills1, Timesheetinfo, Bankdetails
from . import serializers



# Employee Views.

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee1.objects.all()
    serializer_class = serializers.EmployeeSerializer




# CompensationInfo Views.

class CompensationViewSet(viewsets.ModelViewSet):
    queryset = Compensationinfo.objects.all()
    serializer_class = serializers.CompensationInfoSerializer



# Contact views

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact1.objects.all()
    serializer_class = serializers.ContactSerializer



# Emergency contact views.

class EmergencyContactViewSet(viewsets.ModelViewSet):
    queryset = Emergencycontact.objects.all()
    serializer_class = serializers.EmergencySerializer



# Experience Views.

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience1.objects.all()
    serializer_class = serializers.ExperienceSerializer



# JobInfo Views.

class JobInfoViewSet(viewsets.ModelViewSet):
    queryset = Jobinfo.objects.all()
    serializer_class = serializers.JobInfoSerializer



# LeaveInfo Views.

class LeaveInfoViewSet(viewsets.ModelViewSet):
    queryset = Leaveinfo.objects.all()
    serializer_class = serializers.LeaveInfoSerializer


# ManagementInfo Views.

class ManagementInfoViewSet(viewsets.ModelViewSet):
    queryset = Managementinfo.objects.all()
    serializer_class = serializers.ManagementInfoSerializer


# NationalInfo Views.

class NationalInfoViewSet(viewsets.ModelViewSet):
    queryset = Nationalinfo.objects.all()
    serializer_class = serializers.NationalInfoSerializer


# Organization Views.

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization1.objects.all()
    serializer_class = serializers.OrganizationSerializer



# PersonalInfo Views.

class PersonalInfoViewSet(viewsets.ModelViewSet):
    queryset = Personalinfo.objects.all()
    serializer_class = serializers.PersonalInfoSerializer



# Qualification Views.

class QualificationViewSet(viewsets.ModelViewSet):
    queryset = Qualification1.objects.all()
    serializer_class = serializers.QualificationSerializer



# Skills Views.

class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skills1.objects.all()
    serializer_class = serializers.SkillsSerializer



# TimeSheetInfo Views.

class TimeSheetInfoViewSet(viewsets.ModelViewSet):
    queryset = Timesheetinfo.objects.all()
    serializer_class = serializers.TimeSheetSerializer


# BankDetails Views.

class BankDetailsViewSet(viewsets.ModelViewSet):
    queryset = Bankdetails.objects.all()
    serializer_class = serializers.BankDetailsSerializer


