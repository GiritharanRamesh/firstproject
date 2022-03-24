from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import ContactTable
from .serializers import ContactSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def contact_tableApi(request, id=0):
    if request.method == 'GET':
        Contact = ContactTable.objects.all()
        contact_table_serializer = ContactSerializer(Contact, many=True)
        return JsonResponse(contact_table_serializer.data, safe=False)
    elif request.method == 'POST':
        Contact_data = JSONParser().parse(request)
        contact_table_serializer = ContactSerializer(data=Contact_data)
        if contact_table_serializer.is_valid():
            contact_table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        Contact_data = JSONParser().parse(request)
        Contact = ContactTable.objects.get(emp=Contact_data['emp'])
        contact_table_serializer=ContactSerializer(Contact, data=Contact_data)
        if contact_table_serializer.is_valid():
            contact_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        Contact = ContactTable.objects.get(emp=id)
        Contact.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe = False)
