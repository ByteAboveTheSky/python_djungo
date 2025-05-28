from django.db import models
from django.urls import reverse

class Restaurant(models.Model):
    place_name = models.CharField(max_length=250)
    cuisine = models.CharField(max_length=100, blank=True)
    image_url = models.URLField(blank=True)
    rating = models.FloatField(max_length=5, blank=True)
    price = models.IntegerField(blank=True)
    street = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=10, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    site_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.place_name},{self.city}"

    def get_absolute_url(self):
        return reverse('detail-view', kwargs={"pk": self.id})