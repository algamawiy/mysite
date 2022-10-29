from django.urls import path
from .views import userInfo

urlpatterns = [
    path('user-info/', userInfo),
]
