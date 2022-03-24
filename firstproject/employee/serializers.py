from .models import EmployeeTable
from rest_framework import serializers
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTable
        fields = ('emp_id', 'effective_start_date', 'effective_end_date', 'last_updated_by', 'last_updated_date', 'hire_date', 'ok_to_rehire', 'termination_date', 'benefits_start_date', 'benefits_end_date', 'is_effective', 'total_years_of_experience', 'action')