from django.contrib import admin

from bikes.models import Bike, BikeCategory  # , BikeImages

admin.site.register(BikeCategory)
admin.site.register(Bike)
