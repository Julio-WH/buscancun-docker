from django.db import models

# Create your models here.

class Chofer(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    apellidos = models.CharField('Apellidos', max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
