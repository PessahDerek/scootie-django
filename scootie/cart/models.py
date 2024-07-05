from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20)  # Increased length for phone number

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Cart(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='cart_set')  # Many carts for one client
    items = models.ManyToManyField('CartItem', related_name='cart_items')

    def __str__(self):
        return f'{self.id}'


class CartItem(models.Model):
    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='item')
    bike_id = models.IntegerField()
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    qty = models.IntegerField()
    price = models.IntegerField()
    discount = models.IntegerField()

    def __str__(self):
        return f'{self.id}: {self.model}'
