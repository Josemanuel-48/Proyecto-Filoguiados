from django.db import models

# Create your models here.

# se crea la clase RegistroParada que representa un evento de parada de un carro en un segmento específico.
class RegistroParada(models.Model):
    # se crean los campos de la clase, que corresponden a las columnas de la tabla en la base de datos.
    id_carro = models.CharField(max_length=100)
    sensor   = models.CharField(max_length=100)
    duracion = models.IntegerField()
    hora     = models.DateTimeField()
