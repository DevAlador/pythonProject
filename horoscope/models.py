from django.db import models


class Zodiac(models.Model):


    names = models.CharField(max_length=200)
    information = models.CharField(max_length=500)
