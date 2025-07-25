from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet, VisitLogViewSet, RewardViewSet

router = DefaultRouter()
router.register('vendors', VendorViewSet)
router.register('visits', VisitLogViewSet)
router.register('rewards', RewardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
