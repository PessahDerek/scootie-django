from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from bikes.models import Bike, BikeCategory
from libs.paginator import CustomPagination
from .serializers import BikeSerializer, BikeCategorySerializer


# Create your views here.
class BikeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Bikes to be viewed or edited.
    """
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
    pagination_class = CustomPagination

    @action(methods=['GET'], detail=False, url_name='by-category-page', url_path="by-category-page")
    def by_category(self, request, pk=None):
        """
        Get bikes filtered by category
        """
        category = self.request.query_params.get('category', None)
        category_id = BikeCategory.objects.filter(category=category)
        if len(category_id) == 1:
            print(f"Category: {category_id[0].id}")
            queryset = self.queryset.filter(category=category_id[0].id)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if category is None:
            return Response({'error': "Broken request"}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': "Sorry, we could not find this category!"}, status=status.HTTP_400_BAD_REQUEST)

    class Meta:
        ordering = ['id']


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Categories to be viewed or edited.
    """
    queryset = BikeCategory.objects.all()
    serializer_class = BikeCategorySerializer
