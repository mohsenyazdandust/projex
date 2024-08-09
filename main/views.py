from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers

class CheckCreateStudent(APIView):
    def post(self, request, format=None):
        serializer = serializers.StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance, created = serializer.get_or_create()
        
        if created:
            return Response(serializers.StudentSerializer(instance).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.StudentSerializer(instance).data, status=status.HTTP_200_OK)