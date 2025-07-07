from django.db import models

class Docente(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    materia = models.CharField(max_length=100)
    correo = models.EmailField()

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
