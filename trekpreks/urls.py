from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('loyalty.urls')),
    path('api/users/', include('users.urls')),   # users অ্যাপের URL ইনক্লুড করা হলো
]
