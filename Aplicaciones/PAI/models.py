from django.db import models
from Aplicaciones.Estudiantes.models import Estudiante  # Asegúrate de usar la ruta correcta

class PAI(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    objetivos = models.TextField()
    acciones = models.TextField()

    def __str__(self):
        return f'PAI - {self.estudiante.nombres} {self.estudiante.apellidos}'
