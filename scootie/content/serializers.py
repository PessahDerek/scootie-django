from rest_framework import serializers
from .models import Content, Review, Video, Faq, Contact


class ContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Content
        fields = "__all__"


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"


class FaqSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Faq
        fields = "__all__"


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
