from django.contrib import admin
#import models here
from .models import Flower, Watering, Fertilizer

# Register your models here.
admin.site.register(Flower)
admin.site.register(Watering)
admin.site.register(Fertilizer)