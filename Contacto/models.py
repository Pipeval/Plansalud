from django.db import models

# Create your models here.

class Personas(models.Model):
    nombre = models.CharField(max_length=150)
    telefono = models.CharField(max_length=11)
    email = models.EmailField()

class Clientes(models.Model):
    Nombre = models.CharField(max_length=250)
    Telefono = models.CharField(max_length=15)
    Email = models.EmailField(max_length=250, default='prueba@prueba.cl')
    Renta = models.CharField(max_length=20)
    Prevision = models.CharField(max_length=250)
    Region = models.CharField(max_length=250)
    Cargas = models.CharField(max_length=20)





