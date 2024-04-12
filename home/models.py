from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    price = models.FloatField(null=True, blank=True)
    city = models.CharField(max_length=200)
    postal_code = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    url = models.CharField(max_length=30)
    picture = models.ImageField(upload_to="home/static/images/events", null=True, blank=True)
    display = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Picture(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="home/static/images/galerie")
    display = models.BooleanField(default=True)

    def __str__(self):
        return self.title
# Create your models here.
