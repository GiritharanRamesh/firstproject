from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import NationalInfoTable
from .serializers import NationalInfoSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def national_info_tableApi(request, id=0):
    if request.method == 'GET':
        NationalInfo = NationalInfoTable.objects.all()
        national_info_table_serializer = NationalInfoSerializer(NationalInfo, many=True)
        return JsonResponse(national_info_table_serializer.data, safe=False)
    elif request.method == 'POST':
        National_info_data = JSONParser().parse(request)
        national_info_table_serializer = NationalInfoSerializer(data=National_info_data)
        if national_info_table_serializer.is_valid():
            national_info_table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        National_info_data = JSONParser().parse(request)
        NationalInfo = NationalInfoTable.objects.get(emp=National_info_data['emp'])
        national_info_table_serializer=NationalInfoSerializer(NationalInfo, data=National_info_data)
        if national_info_table_serializer.is_valid():
            national_info_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        NationalInfo = NationalInfoTable.objects.get(emp=id)
        NationalInfo.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe = False)
