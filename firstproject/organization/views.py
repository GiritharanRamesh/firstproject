from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import OrganizationTable
from .serializers import OrganizationSerializer

from django.core.files.storage import default_storage


# Create your views here.

@csrf_exempt
def organization_tableApi(request, id=0):
    if request.method == 'GET':
        Organization = OrganizationTable.objects.all()
        organization_table_serializer = OrganizationSerializer(Organization, many=True)
        return JsonResponse(organization_table_serializer.data, safe=False)
    elif request.method == 'POST':
        Organization_data = JSONParser().parse(request)
        organization_table_serializer = OrganizationSerializer(data=Organization_data)
        if organization_table_serializer.is_valid():
            organization_table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        Organization_data = JSONParser().parse(request)
        Organization = OrganizationTable.objects.get(emp=Organization_data['emp'])
        organization_table_serializer = OrganizationSerializer(Organization, data=Organization_data)
        if organization_table_serializer.is_valid():
            organization_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        Organization = OrganizationTable.objects.get(emp=id)
        Organization.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)

