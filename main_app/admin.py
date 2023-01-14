from django.contrib import admin
#import models here
from .models import Flower

# Register your models here.
admin.site.register(Flower)