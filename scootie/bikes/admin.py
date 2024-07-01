from django.contrib import admin

from bikes.models import Bike, BikeCategory  # , BikeImages
from content.models import Content

admin.site.register(BikeCategory)
admin.site.register(Bike)
admin.site.register(Content)
