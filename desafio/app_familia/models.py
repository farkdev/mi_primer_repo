from django.db import models

# Create your models here.

class Familias (models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    nacimiento = models.DateField()
    vinculo = models.CharField(max_length=20)