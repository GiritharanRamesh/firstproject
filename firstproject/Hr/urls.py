from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, CompensationViewSet, ContactViewSet, EmergencyContactViewSet, LeaveInfoViewSet

router = DefaultRouter()
router.register('/Employee', EmployeeViewSet)
"""router.register('/CompensationInfo', CompensationViewSet),
router.register('/Contact', ContactViewSet),
router.register('/EmergencyContact', EmergencyContactViewSet),
router.register('/LeaveInfo', LeaveInfoViewSet)"""

from django.urls import path, include

urlpatterns = [
    path('Employee/', include(router.urls)),
    """path('CompensationInfo/', include(router.urls)),
    path('Contact/', include(router.urls)),
    path('EmergencyContact/', include(router.urls)),
    path('LeaveInfo/', include(router.urls)),"""
]