from rest_framework import serializers

from .models import Bike, BikeCategory  # , BikeImages


class BikeCategoryNameSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return instance.category

    class Meta:
        model = Bike
        fields = ['category']


class BikeSerializer(serializers.HyperlinkedModelSerializer):
    category = BikeCategoryNameSerializer(read_only=True)

    class Meta:
        model = Bike
        fields = '__all__'


class BikeCategorySerializer(serializers.HyperlinkedModelSerializer):
    bikes = BikeSerializer(many=True, read_only=True)

    class Meta:
        model = BikeCategory
        fields = ['category', 'bikes']
