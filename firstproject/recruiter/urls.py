from rest_framework.routers import DefaultRouter
from .views import ProspectCandidateViewSet

router = DefaultRouter()
router.register('/ProspectCandidate', ProspectCandidateViewSet)

from django.urls import path, include

urlpatterns = [
    path('ProspectCandidate/', include(router.urls))
]
