from django.db import models

# Create your models here.
class Producto(models.Model):

    imagen = models.ImageField
    titulo = models.CharField
    descripcion = models.CharField
    contenido = models.CharField
    precio = models.BigIntegerField