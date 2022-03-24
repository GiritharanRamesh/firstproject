"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""

from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('', include('bank_details.urls')),
    path('', include('compensation_info.urls')),
    path('', include('contact.urls')),
    path('', include('emergency_contact.urls')),
    path('', include('experience.urls')),
    path('', include('job_info.urls')),
    path('', include('management_info.urls')),
    path('', include('national_info.urls')),
    path('', include('organization.urls')),
    path('', include('personal_info.urls')),
    path('', include('employee.urls')),
    path('', include('leave_progress.urls')),
    path('', include('qualification.urls')),
    path('', include('skills.urls')),
    path('', include('time_sheet.urls')),
    path('', include('Hr.urls')),
    path('', include('recruiter.urls'))
]