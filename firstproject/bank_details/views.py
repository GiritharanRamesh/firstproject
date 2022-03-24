from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import BankDetailsTable
from .serializers import BankDetailsSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def bankdetails_tableApi(request, id=0):
    if request.method == 'GET':
        BankDetails = BankDetailsTable.objects.all()
        bank_details_table_serializer = BankDetailsSerializer(BankDetails, many=True)
        return JsonResponse(bank_details_table_serializer.data, safe=False)
    elif request.method == 'POST':
        BankDetails_data = JSONParser().parse(request)
        bank_details_table_serializer = BankDetailsSerializer(data=BankDetails_data)
        if bank_details_table_serializer.is_valid():
            bank_details_table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        BankDetails_data = JSONParser().parse(request)
        BankDetails = BankDetailsTable.objects.get(emp=BankDetails_data['emp'])
        bank_details_table_serializer=BankDetailsSerializer(BankDetails, data=BankDetails_data)
        if bank_details_table_serializer.is_valid():
            bank_details_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        BankDetails = BankDetailsTable.objects.get(emp=id)
        BankDetails.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe = False)
