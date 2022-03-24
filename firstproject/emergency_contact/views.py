from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import EmergencyTable
from .serializers import EmergencySerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def emergency_tableApi(request, id=0):
    if request.method == 'GET':
        Emergency = EmergencyTable.objects.all()
        emergency_table_serializer = EmergencySerializer(Emergency, many=True)
        return JsonResponse(emergency_table_serializer.data, safe=False)
    elif request.method == 'POST':
        Emergency_data = JSONParser().parse(request)
        emergency_table_serializer = EmergencySerializer(data=Emergency_data)
        if emergency_table_serializer.is_valid():
            emergency_table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        Emergency_data = JSONParser().parse(request)
        Emergency = EmergencyTable.objects.get(emp=Emergency_data['emp'])
        emergency_table_serializer=EmergencySerializer(Emergency, data=Emergency_data)
        if emergency_table_serializer.is_valid():
            emergency_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        Emergency = EmergencyTable.objects.get(emp=id)
        Emergency.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe = False)
