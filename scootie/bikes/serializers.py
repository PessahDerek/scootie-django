from rest_framework import serializers

from .models import Bike, BikeCategory  # , BikeImages


class BikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bike
        fields = '__all__'


class BikeCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BikeCategory
        fields = "__all__"
