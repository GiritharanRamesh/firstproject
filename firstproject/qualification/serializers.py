from .models import QualificationTable
from rest_framework import serializers
class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualificationTable
        fields = ('class_field', 'mark_percentage', 'pass_out_year', 'location', 'institution_name')