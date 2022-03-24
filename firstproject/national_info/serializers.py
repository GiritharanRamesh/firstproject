from .models import NationalInfoTable
from rest_framework import serializers
class NationalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NationalInfoTable
        fields = ('national_id', 'card_type', 'action', 'last_updated_by', 'last_updated_date')