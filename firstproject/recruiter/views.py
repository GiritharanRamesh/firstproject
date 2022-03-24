from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import ProspectCandidate
from .serializers import ProspectCandidateSerializer

from django.core.files.storage import default_storage


# Create your views here.

@csrf_exempt
def prospectcandidate_Api(request, id=0):
    if request.method == 'GET':
        Prospect_Candidate = ProspectCandidate.objects.all()
        prospect_candidate_serializer = ProspectCandidateSerializer(Prospect_Candidate, many=True)
        return JsonResponse(prospect_candidate_serializer.data, safe=False)
    elif request.method == 'POST':
        Prospect_Candidate_data = JSONParser().parse(request)
        prospect_candidate_serializer = ProspectCandidateSerializer(data=Prospect_Candidate_data)
        if prospect_candidate_serializer.is_valid():
            prospect_candidate_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        Prospect_Candidate_data = JSONParser().parse(request)
        Prospect_candidate = ProspectCandidate.objects.get(emp=Prospect_Candidate_data['emp'])
        prospect_candidate_table_serializer = ProspectCandidateSerializer(Prospect_candidate, data=Prospect_Candidate_data)
        if prospect_candidate_table_serializer.is_valid():
            prospect_candidate_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        Prospect_Candidate = ProspectCandidate.objects.get(emp=id)
        Prospect_Candidate.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)


