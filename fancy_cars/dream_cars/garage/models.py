from django.db import models
from django.urls import reverse
class Car(models.Model):
    make = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    color = models.CharField(max_length=30)
    engin = models.CharField(max_length=30)
    year = models.IntegerField(default=1980)
    image = models.ImageField(upload_to='images/', blank=True, )

    def __str__(self):
        return f"{self.model},{self.year}"
    def get_absolute_url(self):
        return reverse("DetailView", kwargs={"pk": self.id})




# 1969 Dodge Dart GTS 440
# 2017 Pontiac Trans Am Super Duty
# 1968 Mercury Cyclone GT
# 1966 Chevy Biscayne