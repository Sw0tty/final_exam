from django.shortcuts import render
from rest_framework import generics

from tourism_app.models import Tourist
from tourism_app.serializers import TouristSerializer


class TouristAPIView(generics.CreateAPIView):
    model = Tourist
    serializer_class = TouristSerializer
