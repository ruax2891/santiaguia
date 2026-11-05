from django.db import models

# Create your models here.

class Pregunta(models.Model):
    texto = models.CharField(max_length=100)

class Respuesta(models.Model):
    pregunta_original = models.CharField(max_length=100)
    pagina_contribucion = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    texto = models.TextField()
    fuentes = models.TextField()