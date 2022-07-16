from django.db import models
from datetime import date
class Persona(models.Model):
    nombre = models.CharField(max_length=50, default="")
    edad = models.IntegerField(default=12)
    SEX = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('N', 'No se dice')
    )
    sexo = models.CharField(max_length=1,choices=SEX, default='N')
    clan = models.CharField(max_length=50, default='Konoha')
    fecha_nacimiento = models.DateField(default=date(1,1,1))
