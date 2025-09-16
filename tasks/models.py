from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    fecha_creacion = models.DateField()
    entrenador = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre