from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import LeaveProgressTable
from .serializers import LeaveInfoSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def leave_info_tableApi(request, id=0):
    if request.method == 'GET':
        LeaveInfo = LeaveProgressTable.objects.all()
        leave_info_table_serializer = LeaveInfoSerializer(LeaveInfo, many=True)
        return JsonResponse(leave_info_table_serializer.data, safe=False)
    elif request.method == 'POST':
        Leave_info_data = JSONParser().parse(request)
        leave_info_table_serializer = LeaveInfoSerializer(data=Leave_info_data)
        if leave_info_table_serializer.is_valid():
            leave_info_table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        Leave_info_data = JSONParser().parse(request)
        LeaveInfo = LeaveProgressTable.objects.get(emp_id=Leave_info_data['emp_id'])
        leave_info_table_serializer=LeaveInfoSerializer(LeaveInfo, data=Leave_info_data)
        if leave_info_table_serializer.is_valid():
            leave_info_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        LeaveInfo = LeaveProgressTable.objects.get(emp=id)
        LeaveInfo.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe = False)
