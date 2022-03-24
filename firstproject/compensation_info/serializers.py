from rest_framework import serializers
from .models import CompensationInfoTable

class CompensationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompensationInfoTable
        fields = ('currency', 'basic', 'dearness_allowance', 'hra', 'conveyance_allowance', 'special_allowance', 'salary_advance', 'pf_employee', 'esic_employee', 'pt', 'pf_employer_cont', 'esic_employer_cont', 'is_effective', 'effective_start_date', 'effective_end_date', 'action', 'last_updated_by', 'last_updated_date')