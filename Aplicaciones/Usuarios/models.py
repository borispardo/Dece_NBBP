from django.db import models

ROLES = (
    ('Psicólogo', 'Psicólogo'),
    ('Docente', 'Docente'),
    ('Administrador', 'Administrador'),
    ('Orientador', 'Orientador'),
)

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=20, choices=ROLES)
    correo = models.EmailField(unique=True)
    clave = models.CharField(max_length=128)  # Se recomienda encriptarla

    def __str__(self):
        return f"{self.nombre} - {self.rol}"