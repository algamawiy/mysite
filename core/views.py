from django.shortcuts import render
from .models import UserInfo
from .serializers import UserInfoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def userInfo(request):
    user_info = UserInfo.objects.all()
    serializer = UserInfoSerializer(user_info, many=True)
    return Response(serializer.data)
    
    





