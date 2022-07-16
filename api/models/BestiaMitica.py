from django.db import models
from api.models.Ninja import Ninja
class BestiaMitica(models.Model):
    nombre = models.CharField(max_length=50, default="")
    tipo = models.CharField(max_length=30, default="")
    invocador = models.ForeignKey(Ninja, on_delete=models.SET_NULL,null=True)
