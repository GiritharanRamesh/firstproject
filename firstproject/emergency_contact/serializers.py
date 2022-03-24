from .models import EmergencyTable
from rest_framework import serializers
class EmergencySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyTable
        fields = ('primary_flag', 'relationship', 'name', 'phone', 'action', 'last_updated_by', 'last_updated_date')