from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BikeSerializer, BikeCategorySerializer

from bikes.models import Bike, BikeCategory


# Create your views here.
class BikeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Bikes to be viewed or edited.
    """
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Categories to be viewed or edited.
    """
    queryset = BikeCategory.objects.all()
    serializer_class = BikeCategorySerializer
