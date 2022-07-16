from django.db import models
class Mision(models.Model):
    cliente = models.CharField(max_length=50, default="")
    pais_cliente = models.CharField(max_length=30, default="")
    rango = models.CharField(max_length=1, default='')
    recompensa = models.IntegerField(default=0)
