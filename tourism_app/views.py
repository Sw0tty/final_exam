from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from tourism_app.models import MountainPass
from tourism_app.serializers import MountainPassSerializer, DetailMountainPassSerializer


# class DetailMountainPass(generics.RetrieveUpdateAPIView):
#     queryset = MountainPass.objects.all()
#     serializer_class = DetailMountainPassSerializer


class DetailMountainPass(APIView):
    """
    API endpoint to get detail mountain pass
    Methods: GET, PATCH
    """
    serializer_class = DetailMountainPassSerializer
    model = MountainPass

    def get_object(self, pk):
        return MountainPass.objects.get(pk=pk)
    
    def get_serializer(self, instance):
        return self.serializer_class(instance)
    
    def get(self, request, pk):
        instance = self.get_object(pk)
        return Response(self.serializer_class(instance).data)
    
    def patch(self, request, pk):
        object_instance = self.get_object(pk)

        if object_instance.status != 'new':
            return Response({"state": 0, "message": "Запись должна иметь статус new для редактирования"})

        serializer = self.serializer_class(object_instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"state": 1, "message": "Запись обновлена"})
        return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "Введены недопустимые значения", "message": "Не удалось"})
    

class ListMountainPasses(APIView):
    """
    API endpoint to filter mountain passes
    Methods: GET
    """
    serializer_class = MountainPassSerializer

    def get_queryset(self, query_params):
        queryset = MountainPass.objects.all()
        email_filter = query_params.get('user_email')

        if email_filter:
            queryset = queryset.filter(user__email=email_filter)
        return queryset
    
    def get(self, request):
        queryset = self.get_queryset(request.query_params)
        
        if queryset:
            return Response(self.serializer_class(queryset, many=True).data)
        return Response({"state": 0, "message": "Ничего не найдено"})
    
    
class SubmitData(APIView):
    """
    API endpoint to post new mountain pass
    Methods: POST
    """
    serializer_class = MountainPassSerializer
    model = MountainPass

    def get_serializer(self):
        return self.serializer_class()
    
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": status.HTTP_201_CREATED, "message": "Запись создана", "id": serializer.data['id']})
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "Введены недопустимые значения", "id": None})
        except:
            return Response({"status": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": "Ошибка подключения к базе данных", "id": None})
