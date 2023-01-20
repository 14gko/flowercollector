from django.db import models
from django.urls import reverse
from datetime import date

WATERED = (
    ('Y', 'Yes'),
    ('N', 'No')
)

# COLORS = (('Red', 'Red'), ('Orange', 'Orange'))
# 'Yellow', 'Green', 'Blue', 'Purple', 'Pink', 'White', 'Black')

class Fertilizer(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    # ?
    def get_absolute_url(self):
        return reverse('fert_detail', kwargs={'pk': self.id})

# Create your models here.
class Flower(models.Model):
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    color = models.CharField(
        max_length=50,
        # choices=COLORS,
        # default=COLORS[0]
    )
    description = models.CharField(max_length=250)
    quantity = models.IntegerField()
    fertilizers = models.ManyToManyField(Fertilizer)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'flower_id': self.id})
    
    def watered_today(self):
        watering_today = self.watering_set.filter(date=date.today())
        for w in watering_today:
            if w.watered == 'Y':
                return True
        return False

        # return self.watering_set.filter(date=date.today()).count() > 0
    


class Watering(models.Model):
    date = models.DateField()
    watered = models.CharField(
            max_length=1,
            choices=WATERED,
            default=WATERED[1][0]
            )
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_watered_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']

