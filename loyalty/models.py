from django.db import models
from django.contrib.auth.models import User

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    location_name = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    visits_required = models.IntegerField(default=3)
    cooldown_hours = models.IntegerField(default=24)

    def __str__(self):
        return self.name

class VisitLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    duration_minutes = models.FloatField()

class Reward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    unlocked = models.BooleanField(default=False)
    redeemed = models.BooleanField(default=False)
    redeemed_at = models.DateTimeField(null=True, blank=True)

class RedemptionLog(models.Model):
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)
    redeemed_at = models.DateTimeField(auto_now_add=True)
    location_verified = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
