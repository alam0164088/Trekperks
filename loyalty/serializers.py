from rest_framework import serializers
from .models import Vendor, VisitLog, Reward, RedemptionLog

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class VisitLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitLog
        fields = '__all__'

class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = '__all__'

class RedemptionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedemptionLog
        fields = '__all__'
