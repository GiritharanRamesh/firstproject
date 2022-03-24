from .models import ManagementInfoTable
from rest_framework import serializers
class ManagementInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagementInfoTable
        fields = ('manager_emp_id', 'first_name', 'last_name', 'work_phone', 'manager_email', 'is_effective', 'effective_start_date', 'effective_end_date', 'action', 'last_updated_by', 'last_updated_date')