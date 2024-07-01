from django.shortcuts import render
from rest_framework import viewsets

from content.models import Content, Review
from content.serializers import ContentSerializer, ReviewSerializer


# Create your views here.
class ContentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows site content to be viewed or edited.
    """
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class ReviewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reviews to be viewed or edited.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
