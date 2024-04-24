from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    intro = models.TextField()
    description = models.TextField()
    date = models.DateTimeField()
    price = models.FloatField(null=True, blank=True)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    url = models.CharField(max_length=30)
    picture = models.ImageField(upload_to="images/events", null=True, blank=True)
    flyer = models.ImageField(upload_to="images/events")


    def __str__(self):
        return self.title


class Picture(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="images/galerie")
    display = models.BooleanField(default=True)
    carrousel = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Contact(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.nom
# Create your models here.
