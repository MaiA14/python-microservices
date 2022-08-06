from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=200)
    year = models.PositiveBigIntegerField(default=2000)
    image = models.CharField(max_length=200)

class User(models.Model):
    pass

