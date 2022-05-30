from django.db import models
from django.db import models

class Yo(models.Model):
    miNombreCompleto = models.CharField(max_length=30, default='x')
    miEdad = models.IntegerField(default=1)
class Familiar(models.Model):
    NombreCompleto = models.CharField(max_length=30, default='z')
    Edad = models.IntegerField(default=1)
    mismaSangre= models.CharField(max_length = 20,default='')
    relacion = models.CharField(max_length=20, default='')    
