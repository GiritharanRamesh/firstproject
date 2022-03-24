from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import EmployeeTable
from .serializers import EmployeeSerializer

from django.core.files.storage import default_storage


# Create your views here.

@csrf_exempt
def employee_tableApi(request, id=0):
    if request.method == 'GET':
        Employee = EmployeeTable.objects.all()
        employee_table_serializer = EmployeeSerializer(Employee, many=True)
        return JsonResponse(employee_table_serializer.data, safe=False)
    elif request.method == 'POST':
        Employee_data = JSONParser().parse(request)
        employee_table_serializer = EmployeeSerializer(data=Employee_data)
        if employee_table_serializer.is_valid():
            employee_table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        Employee_data = JSONParser().parse(request)
        Employee = EmployeeTable.objects.get(emp=Employee_data['emp'])
        employee_table_serializer = EmployeeSerializer(Employee, data=Employee_data)
        if employee_table_serializer.is_valid():
            employee_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        Employee = EmployeeTable.objects.get(emp=id)
        Employee.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
