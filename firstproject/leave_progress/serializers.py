from .models import LeaveProgressTable
from rest_framework import serializers
class LeaveInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveProgressTable
        fields = ('year', 'leave_balance', 'leaves_availed', 'emp_id')