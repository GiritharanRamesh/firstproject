from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import ExperienceTable
from .serializers import ExperienceSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def experience_tableApi(request, id=0):
    if request.method == 'GET':
        Experience = ExperienceTable.objects.all()
        experience_table_serializer = ExperienceSerializer(Experience, many=True)
        return JsonResponse(experience_table_serializer.data, safe=False)
    elif request.method == 'POST':
        Experience_data = JSONParser().parse(request)
        experience_table_serializer = ExperienceSerializer(data=Experience_data)
        if experience_table_serializer.is_valid():
            experience_table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        Experience_data = JSONParser().parse(request)
        Experience = ExperienceTable.objects.get(emp=Experience_data['emp'])
        experience_table_serializer=ExperienceSerializer(Experience, data=Experience_data)
        if experience_table_serializer.is_valid():
            experience_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        Experience = ExperienceTable.objects.get(emp=id)
        Experience.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe = False)
