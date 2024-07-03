from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import BikeSerializer, BikeCategorySerializer

from bikes.models import Bike, BikeCategory


# Create your views here.
class BikeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Bikes to be viewed or edited.
    """
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer

    @action(methods=['GET'], detail=False, url_name='by-category', url_path="by-category")
    def by_category(self, request, pk=None):
        """
        Get bikes filtered by category
        """
        category = self.request.query_params.get('category', None)
        category_id = BikeCategory.objects.filter(category=category)
        if len(category_id) == 1:
            print(f"Category: {category_id[0].id}")
            queryset = self.queryset.filter(category=1)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if category is None:
            return Response({'error': "Broken request"}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': "Sorry, we could not find this category!"}, status=status.HTTP_400_BAD_REQUEST)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Categories to be viewed or edited.
    """
    queryset = BikeCategory.objects.all()
    serializer_class = BikeCategorySerializer
