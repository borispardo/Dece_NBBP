from django.db import models
from Aplicaciones.Estudiantes.models import Estudiante

class CasoIntervencion(models.Model):
    ESTADO_CHOICES = [
        ('Abierto', 'Abierto'),
        ('En seguimiento', 'En seguimiento'),
        ('Cerrado', 'Cerrado'),
    ]

    MOTIVO_CHOICES = [
        ('Emocional', 'Emocional'),
        ('Aprendizaje', 'Aprendizaje'),
    ]

    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha_apertura = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    motivo = models.CharField(max_length=20, choices=MOTIVO_CHOICES)
    descripcion = models.TextField()

    def __str__(self):
        return f'Caso de {self.estudiante.nombres} - {self.estado}'
