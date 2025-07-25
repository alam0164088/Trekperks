from django.contrib import admin
from .models import Vendor, VisitLog, Reward, RedemptionLog

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location_name', 'latitude', 'longitude', 'visits_required', 'cooldown_hours')
    search_fields = ('name', 'location_name')

@admin.register(VisitLog)
class VisitLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'vendor', 'timestamp', 'duration_minutes')
    list_filter = ('timestamp', 'vendor')
    search_fields = ('user__username', 'vendor__name')

@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'vendor', 'unlocked', 'redeemed', 'redeemed_at')
    list_filter = ('unlocked', 'redeemed')
    search_fields = ('user__username', 'vendor__name')

@admin.register(RedemptionLog)
class RedemptionLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'reward', 'redeemed_at', 'location_verified')
    list_filter = ('location_verified',)
    search_fields = ('reward__user__username',)
