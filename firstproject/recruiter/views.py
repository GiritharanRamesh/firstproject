from rest_framework import viewsets
from .models import ProspectCandidate
from . import serializers

class ProspectCandidateViewSet(viewsets.ModelViewSet):
    queryset = ProspectCandidate.objects.all()
    serializer_class = serializers.ProspectCandidateSerializer


