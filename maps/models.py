from django.db import models

# Create your models here.
class InterestLocation(models.Model):
    nombre = models.CharField(max_length=50, default="Lugar Desconocido")
    comuna = models.CharField(max_length=50, default="Comuna Desconocida")
    tipo = models.CharField(max_length=50, default="Miscelaneo")
    encontrables = models.CharField(max_length=200, default="Sin detalles")
    razonvisita = models.CharField(max_length=200, default="Sin especificar")

    latitud = models.FloatField(default=-33.5)
    longitud = models.FloatField(default=-70.5)