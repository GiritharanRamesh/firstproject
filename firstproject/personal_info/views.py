from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import PersonalInfoTable
from .serializers import PersonalInfoSerializer

from django.core.files.storage import default_storage


# Create your views here.

@csrf_exempt
def personal_info_tableApi(request, id=0):
    if request.method == 'GET':
        PersonalInfo = PersonalInfoTable.objects.all()
        personal_info_table_serializer = PersonalInfoSerializer(PersonalInfo, many=True)
        return JsonResponse(personal_info_table_serializer.data, safe=False)
    elif request.method == 'POST':
        Personal_Info_data = JSONParser().parse(request)
        personal_info_table_serializer = PersonalInfoSerializer(data=Personal_Info_data)
        if personal_info_table_serializer.is_valid():
            personal_info_table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        Personal_Info_data = JSONParser().parse(request)
        PersonalInfo = PersonalInfoTable.objects.get(emp=Personal_Info_data['emp'])
        personal_info_table_serializer = PersonalInfoSerializer(PersonalInfo, data=Personal_Info_data)
        if personal_info_table_serializer.is_valid():
            personal_info_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        PersonalInfo = PersonalInfoTable.objects.get(emp=id)
        PersonalInfo.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
