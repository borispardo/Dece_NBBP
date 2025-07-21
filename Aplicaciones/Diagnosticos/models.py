from django.db import models
from Aplicaciones.Estudiantes.models import Estudiante  # Asegúrate de usar la ruta correcta

class Diagnostico(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return f'{self.tipo} - {self.estudiante.nombres} {self.estudiante.apellidos}'

