# users/urls.py

from django.urls import path
from .views import RegisterView  # ধরছি তোমার views.py তে RegisterView আছে

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]
