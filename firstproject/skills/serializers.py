from .models import SkillsTable
from rest_framework import serializers
class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillsTable
        fields = ('is_primary', 'technology', 'years_of_experience', 'last_used', 'certified')