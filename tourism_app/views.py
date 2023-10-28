from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from tourism_app.models import MountainPass
from tourism_app.serializers import MountainPassSerializer


class MountainPassAPIView(generics.CreateAPIView):
    queryset = MountainPass.objects.all()
    serializer_class = MountainPassSerializer


class SubmitData(APIView):
    """
    API endpoint to get mountains passes and post new
    """
    serializer_class = MountainPassSerializer
    model = MountainPass

    def get_queryset(self):
        return MountainPass.objects.all()
    
    def get_serializer(self):
        return self.serializer_class()
    
    def get(self, request):
        queryset = self.get_queryset()
        return Response(self.serializer_class(queryset, many=True).data)
    
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": status.HTTP_201_CREATED, "message": "Запись создана", "id": serializer.data['id']})
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "Введены недопустимые значения", "id": None})
        except:
            return Response({"status": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": "Ошибка подключения к базе данных", "id": None})
