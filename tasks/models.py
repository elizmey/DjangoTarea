from django.db import models
from django.contrib.auth.models import User

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    entrenador = models.CharField(max_length=100, blank=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + ' - por ' + self.usuario.username