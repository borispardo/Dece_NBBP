from django.db import models
from Aplicaciones.Estudiantes.models import Estudiante

class Diagnostico(models.Model):
    TIPOS_CHOICES = [
        ('Emocional', 'Emocional'),
        ('Conductual', 'Conductual'),
        ('Aprendizaje', 'Aprendizaje'),
        ('Familiar', 'Familiar'),
        ('Otro', 'Otro'),
    ]

    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50, choices=TIPOS_CHOICES)
    descripcion = models.TextField()

    def __str__(self):
        return f'{self.estudiante} - {self.tipo}'
