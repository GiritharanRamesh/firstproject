from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import TimeSheetInfoTable
from .serializers import TimeSheetSerializer

from django.core.files.storage import default_storage


# Create your views here.

@csrf_exempt
def time_sheet_tableApi(request, id=0):
    if request.method == 'GET':
        Time_Sheet = TimeSheetInfoTable.objects.all()
        time_sheet_table_serializer = TimeSheetSerializer(Time_Sheet, many=True)
        return JsonResponse(time_sheet_table_serializer.data, safe=False)
    elif request.method == 'POST':
        Time_Sheet_data = JSONParser().parse(request)
        time_sheet_table_serializer = TimeSheetSerializer(data=Time_Sheet_data)
        if time_sheet_table_serializer.is_valid():
            time_sheet_table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        Time_Sheet_data = JSONParser().parse(request)
        Time_Sheet = TimeSheetInfoTable.objects.get(emp=Time_Sheet_data['emp'])
        time_sheet_table_serializer = TimeSheetSerializer(Time_Sheet, data=Time_Sheet_data)
        if time_sheet_table_serializer.is_valid():
            time_sheet_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        Time_Sheet = TimeSheetInfoTable.objects.get(emp=id)
        Time_Sheet.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
