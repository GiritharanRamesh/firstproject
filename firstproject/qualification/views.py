from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import QualificationTable
from .serializers import QualificationSerializer

from django.core.files.storage import default_storage


# Create your views here.

@csrf_exempt
def qualification_tableApi(request, id=0):
    if request.method == 'GET':
        Qualification = QualificationTable.objects.all()
        qualification_table_serializer = QualificationSerializer(Qualification, many=True)
        return JsonResponse(qualification_table_serializer.data, safe=False)
    elif request.method == 'POST':
        Qualification_data = JSONParser().parse(request)
        qualification_table_serializer = QualificationSerializer(data=Qualification_data)
        if qualification_table_serializer.is_valid():
            qualification_table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        Qualification_data = JSONParser().parse(request)
        Qualification = QualificationTable.objects.get(emp=Qualification_data['emp'])
        qualification_table_serializer = QualificationSerializer(Qualification, data=Qualification_data)
        if qualification_table_serializer.is_valid():
            qualification_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        Qualification = QualificationTable.objects.get(emp=id)
        Qualification.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
