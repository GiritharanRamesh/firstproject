from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import CompensationInfoTable
from .serializers import CompensationInfoSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def compensationinfo_tableApi(request, id=0):
    if request.method == 'GET':
        CompensationInfo = CompensationInfoTable.objects.all()
        compensation_info_serializer = CompensationInfoSerializer(CompensationInfo, many=True)
        return JsonResponse(compensation_info_serializer.data, safe=False)
    elif request.method == 'POST':
        Compensationinfo_data = JSONParser().parse(request)
        compensation_info_serializer = CompensationInfoSerializer(data=Compensationinfo_data)
        if compensation_info_serializer.is_valid():
            compensation_info_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        Compensationinfo_data = JSONParser().parse(request)
        CompensationInfo = CompensationInfoTable.objects.get(emp=Compensationinfo_data['emp'])
        compensation_info_serializer=CompensationInfoSerializer(CompensationInfo, data=Compensationinfo_data)
        if compensation_info_serializer.is_valid():
            compensation_info_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        CompensationInfo = CompensationInfoTable.objects.get(emp=id)
        CompensationInfo.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe = False)




