from rest_framework import serializers
from .models import BankDetailsTable

class BankDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankDetailsTable
        fields = ('id', 'bank_name', 'branch', 'account_number', 'ifsc_code', 'beneficiary_name', 'account_type', 'routing_number')