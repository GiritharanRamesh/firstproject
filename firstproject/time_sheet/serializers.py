from .models import TimeSheetInfoTable
from rest_framework import serializers
class TimeSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSheetInfoTable
        fields = ('week_start_date', 'monday', 'sunday')