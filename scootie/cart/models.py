from django.core.validators import MinValueValidator
from django.db import models
from bikes.models import Bike


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)

    def __get__(self, instance, owner):
        if instance is not None:
            return instance

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='carts')

    def __str__(self):
        return f"{self.customer.first_name}'s cart"


class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=20, default='black')
    qty = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    price = models.IntegerField(validators=[MinValueValidator(1)])
    discount = models.IntegerField(validators=[MinValueValidator(1)])
    subtotal = models.IntegerField(validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model}"
