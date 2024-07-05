from django.db import models


# Create your models here.
class BikeCategory(models.Model):
    category = models.CharField(max_length=50)

    def __get__(self, instance, owner):
        instance.bikes = Bike.objects.filter(category=self.category)
        return instance

    def __str__(self):
        return self.category + f" :{len(self.bikes.all())}"

    class Meta:
        ordering = ['id']


class Bike(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    category = models.ForeignKey(BikeCategory, related_name='bikes', on_delete=models.CASCADE)
    frame = models.CharField(max_length=50)
    image1 = models.ImageField(upload_to='bike_images', null=False, blank=False)
    image2 = models.ImageField(upload_to='bike_images', null=True, blank=True)
    image3 = models.ImageField(upload_to='bike_images', null=True, blank=True)
    image4 = models.ImageField(upload_to='bike_images', null=True, blank=True)
    image5 = models.ImageField(upload_to='bike_images', null=True, blank=True)
    speed_gear = models.CharField(max_length=50)
    fork = models.CharField(max_length=50)
    max_load = models.IntegerField()
    motor_voltage = models.FloatField()
    motor_power = models.FloatField()
    motor_type = models.CharField(max_length=50)
    range = models.IntegerField()
    display = models.CharField(max_length=50)
    brake = models.CharField(max_length=50)
    battery_voltage = models.FloatField()
    battery_capacity = models.FloatField()
    battery_type = models.CharField(max_length=50)
    tyre_size = models.CharField(max_length=50)
    carton = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    stock = models.IntegerField()
    net_weight = models.FloatField()
    gross_weight = models.FloatField()
    price = models.FloatField()
    discount = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.brand} {self.model}"

    class Meta:
        ordering = ['category']

# class BikeImages(models.Model):
#     src = models.ImageField(upload_to='bike_images/')
#     color = models.CharField(max_length=20)
#     bike = models.ForeignKey(to=Bike, related_name='images', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.src
#
#     def __get__(self, instance, owner):
#         return {"src": self.src, "color": self.color}
