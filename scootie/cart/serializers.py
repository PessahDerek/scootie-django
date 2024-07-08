from rest_framework import serializers

from .models import Customer, Cart, CartItem


class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.HyperlinkedModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'customer', 'items']


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    carts = CartSerializer(many=True)

    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'email', 'carts']
