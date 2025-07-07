from django.db import models
from Aplicaciones.Estudiantes.models import Estudiante

class Representante(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    parentesco = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()

    def __str__(self):
        return f"{self.nombres} {self.apellidos} ({self.parentesco})"
