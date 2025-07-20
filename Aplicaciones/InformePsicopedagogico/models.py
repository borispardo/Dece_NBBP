from django.db import models
from Aplicaciones.Estudiantes.models import Estudiante

class InformePsicopedagogico(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha = models.DateField()
    contenido = models.TextField()
    recomendaciones = models.TextField()

    def _str_(self):
        return f'Informe de {self.estudiante.nombres} - {self.fecha}'