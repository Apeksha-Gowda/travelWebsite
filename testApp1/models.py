from django.db import models
from django.utils import timezone

class Destinations(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    package = models.CharField(max_length=100)
    rating = models.FloatField(default='1')
    image = models.TextField(default='Canada-Montreal')
    date_posted= models.DateTimeField(default=timezone.now)
    hits = models.IntegerField(default=0)

    def __str__(self):
        return self.name