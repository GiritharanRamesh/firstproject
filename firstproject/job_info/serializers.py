from .models import JobInfoTable
from rest_framework import serializers
class JobInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobInfoTable
        fields = ('person_id', 'job_name', 'employee_class', 'employee_type', 'employee_status', 'job_start_date', 'position_start_date', 'is_fulltime_employee', 'job_title', 'position', 'position_name', 'standard_hours', 'cost_center', 'cost_center_name', 'client_based_hire_date', 'destination')