from .models import OrganizationTable
from rest_framework import serializers
class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationTable
        fields = ('organization_type', 'country', 'company', 'company_code', 'company_name', 'account_code', 'account_bt_name', 'address1', 'address2', 'address3', 'city', 'postal_code', 'state')