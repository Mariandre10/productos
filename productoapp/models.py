from django.db import models
from django.utils import timezone


class Producto(models.Model):
    name = models.CharField(max_length=200)
    code = models.IntegerField()
    fabricante = models.CharField(max_length=200)
    origen = models.CharField(max_length=200)
    precio = models.FloatField()
