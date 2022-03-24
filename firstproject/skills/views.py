from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import SkillsTable
from .serializers import SkillsSerializer

from django.core.files.storage import default_storage


# Create your views here.

@csrf_exempt
def skills_tableApi(request, id=0):
    if request.method == 'GET':
        Skills = SkillsTable.objects.all()
        skills_table_serializer = SkillsSerializer(Skills, many=True)
        return JsonResponse(skills_table_serializer.data, safe=False)
    elif request.method == 'POST':
        Skills_data = JSONParser().parse(request)
        skills_table_serializer = SkillsSerializer(data=Skills_data)
        if skills_table_serializer.is_valid():
            skills_table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        Skills_data = JSONParser().parse(request)
        Skills = SkillsTable.objects.get(emp=Skills_data['emp'])
        skills_table_serializer = SkillsSerializer(Skills, data=Skills_data)
        if skills_table_serializer.is_valid():
            skills_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        Skills = SkillsTable.objects.get(emp=id)
        Skills.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
