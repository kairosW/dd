from django.db import models

# Create your models here.

class Solicitud(models.Model):
    ESTADOS = (
        ('PENDIENTE', 'Pendiente'),
        ('ACEPTADA', 'Aceptada'),
        ('RECHAZADA', 'Rechazada'),
        ('EXPIRADA', 'Expirada'),
    )
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    comuna = models.CharField(max_length=50)
    fecha_solicitud = models.DateField(auto_now_add=True)
    fecha_aceptacion = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='PENDIENTE')

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"