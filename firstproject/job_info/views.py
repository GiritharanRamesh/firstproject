from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import JobInfoTable
from .serializers import JobInfoSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def job_info_tableApi(request, id=0):
    if request.method == 'GET':
        JobInfo = JobInfoTable.objects.all()
        job_info_table_serializer = JobInfoSerializer(JobInfo, many=True)
        return JsonResponse(job_info_table_serializer.data, safe=False)
    elif request.method == 'POST':
        Job_info_data = JSONParser().parse(request)
        job_info_table_serializer = JobInfoSerializer(data=Job_info_data)
        if job_info_table_serializer.is_valid():
            job_info_table_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        Job_info_data = JSONParser().parse(request)
        JobInfo = JobInfoTable.objects.get(emp=Job_info_data['emp'])
        job_info_table_serializer=JobInfoSerializer(JobInfo, data=Job_info_data)
        if job_info_table_serializer.is_valid():
            job_info_table_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        JobInfo = JobInfoTable.objects.get(emp=id)
        JobInfo.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe = False)
