from .models import ExperienceTable
from rest_framework import serializers
class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceTable
        fields = ('previous_org_name', 'start_period', 'end_period', 'years_of_experience', 'reference_name', 'reference_contact')