from django.db import models

class ActividadTaller(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
