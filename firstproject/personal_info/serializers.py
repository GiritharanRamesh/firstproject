from .models import PersonalInfoTable
from rest_framework import serializers
class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfoTable
        fields = ('first_name', 'last_name', 'gender', 'dob', 'intial', 'marital_status', 'ethnicity_code', 'is_effective', 'effective_start_date', 'effective_end_date', 'action', 'last_updated_by', 'last_updated_date')