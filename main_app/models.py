from django.db import models

# Create your models here.
class Flower(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name