from django.db import models

class Estudiante(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=10, unique=True)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(blank=True, null=True)
    curso = models.CharField(max_length=50)
    historial = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.curso}"
