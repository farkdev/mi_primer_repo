from django.db import models

# Create your models here.

class Familias (models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    nacimiento = models.DateField()
    vinculo = models.CharField(max_length=20)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Edad: {self.edad} - Nacimiento: {self.nacimiento} - Vinculo: {self.vinculo}"

class Apellido (models.Model):
    Apellido_or = models.CharField(max_length=40)
    Pais = models.CharField(max_length=40)

    def __str__(self):
        return f"Apellido origen: {self.Apellido_or}, Pais: {self.Pais}"

class Domicilio (models.Model):
    Nombre = models.CharField(max_length=40)
    calle = models.CharField(max_length=40)
    viviendo_desde = models.DateField(null=True)

    def __str__(self):
        return f"Nombre: {self.Nombre}, Calle: {self.calle}, Viviendo desde: {self.viviendo_desde}"