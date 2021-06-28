from django.db import models
import datetime


class Artist(models.Model):
    name = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    @property
    def events(self):
        return self.event_set.all()


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=64)
    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    longitude = models.DecimalField(max_digits=22, decimal_places=16)
    date = models.DateField(default=datetime.date.today)
    artists = models.ManyToManyField(Artist)

    def __str__(self):
        return self.name
