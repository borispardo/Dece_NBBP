from django.db import models
from Aplicaciones.CasosIntervencion.models import CasoIntervencion  

class  Cita(models.Model):
    caso = models.ForeignKey(CasoIntervencion, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    profesional = models.CharField(max_length=100)
    observaciones = models.TextField()

    def __str__(self):
        return f'Sesión - {self.fecha.strftime("%Y-%m-%d %H:%M")} ({self.profesional})'