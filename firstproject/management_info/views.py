from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import ManagementInfoTable
from .serializers import ManagementInfoSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def management_info_tableApi(request, id=0):
    if request.method == 'GET':
        ManagementInfo = ManagementInfoTable.objects.all()
        management_info_table_serializer = ManagementInfoSerializer(ManagementInfo, many=True)
        return JsonResponse(management_info_table_serializer.data, safe=False)
    elif request.method == 'POST':
        Management_info_data = JSONParser().parse(request)
        management_info_table_serializer = ManagementInfoSerializer(data=Management_info_data)
        if management_info_table_serializer.is_valid():
            management_info_table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        Management_info_data = JSONParser().parse(request)
        ManagementInfo = ManagementInfoTable.objects.get(emp=Management_info_data['emp'])
        management_info_table_serializer=ManagementInfoSerializer(ManagementInfo, data=Management_info_data)
        if management_info_table_serializer.is_valid():
            management_info_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        ManagementInfo = ManagementInfoTable.objects.get(emp=id)
        ManagementInfo.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe = False)
