from django.db import models

class Gul(models.Model):
    nomi = models.CharField(max_length=10)
    rangi=models.CharField(max_length=16)
