from .models import ProspectCandidate
from rest_framework import serializers
class ProspectCandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProspectCandidate
        fields = ('user', 'skills', 'totalYearsofExp', 'releventExp', 'noticePeriod', 'mobile', 'currentCompany', 'Currentctc', 'expectedCtc', 'currentLoc', 'preferredLoc', 'lastWorkingDay', 'lastUpdatedDate', 'lastUpdatedBy')