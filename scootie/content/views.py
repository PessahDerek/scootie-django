from django.shortcuts import render
from rest_framework import viewsets

from content.models import Content
from content.serializers import ContentSerializer


# Create your views here.
class ContentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows site content to be viewed or edited.
    """
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
