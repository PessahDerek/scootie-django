from rest_framework import serializers
from .models import Cart, Client


class CartSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    client = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'phone', 'email']
