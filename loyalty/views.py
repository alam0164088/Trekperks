from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Vendor, VisitLog, Reward, RedemptionLog
from .serializers import VendorSerializer, VisitLogSerializer, RewardSerializer, RedemptionLogSerializer
from django.utils.timezone import now

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VisitLogViewSet(viewsets.ModelViewSet):
    queryset = VisitLog.objects.all()
    serializer_class = VisitLogSerializer

    def perform_create(self, serializer):
        visit = serializer.save()
        # reward checking logic
        user = visit.user
        vendor = visit.vendor
        valid_visits = VisitLog.objects.filter(user=user, vendor=vendor).count()
        if valid_visits >= vendor.visits_required:
            Reward.objects.get_or_create(user=user, vendor=vendor, unlocked=True)

class RewardViewSet(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer

    @action(detail=True, methods=['post'])
    def redeem(self, request, pk=None):
        reward = self.get_object()
        if reward.redeemed:
            return Response({'message': 'Already redeemed'}, status=400)
        reward.redeemed = True
        reward.redeemed_at = now()
        reward.save()
        RedemptionLog.objects.create(reward=reward, location_verified=True)
        return Response({'message': 'Reward redeemed successfully'})
