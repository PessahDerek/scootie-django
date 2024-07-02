from django.db.models.functions import Length
from django.shortcuts import render
from rest_framework import viewsets

from content.models import Content, Review, Video, Faq, Contact
from content.serializers import ContentSerializer, ReviewSerializer, VideoSerializer, FaqSerializer, ContactSerializer


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

    def get_queryset(self):
        """
        Override default queryset to fetch 10 top-rated reviews.
        """
        queryset = super().get_queryset()  # Get the base queryset
        queryset = queryset.order_by('-rating')[:10]  # Order by rating (highest first) and limit to 10
        return queryset


class VideoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows marketing videos urls to be viewed or edited.
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get_queryset(self):
        """
        Override  default queryset to fetch latest video.
        """
        queryset = super().get_queryset()
        queryset = queryset.order_by('-created_at')
        return queryset


class FaqViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows faqs to be viewed or edited.
    """
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contact us to be viewed or edited.
    """
    queryset = Contact.objects.annotate(
        field_length=Length('contact')
    ).order_by('-field_length')
    serializer_class = ContactSerializer

    # def get_queryset(self):
    #     return Contact.objects.annotate(
    #         field_length=Length('contact')
    #     ).order_by('-field_length')
