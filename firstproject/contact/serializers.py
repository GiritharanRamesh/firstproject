from rest_framework import serializers
from .models import ContactTable

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactTable
        fields = ('phone_no', 'phone_type', 'country_code', 'extension', 'action', 'last_updated_by', 'last_updated_date', 'address_type', 'address1', 'city', 'postal_code', 'state', 'country', 'is_effective', 'effective_start_date', 'effective_end_date')