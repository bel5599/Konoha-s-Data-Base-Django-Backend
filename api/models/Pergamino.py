from django.db import models
from datetime import date
from api.models.Ninja import Ninja
from api.models.Tecnica import Tecnica
class Pergamino(models.Model):
    fecha_sellado = models.DateField(default=date(1,1,1))
    ninja = models.ForeignKey(Ninja, on_delete=models.CASCADE, null=False)
    tecnica = models.ForeignKey(Tecnica, on_delete=models.CASCADE, null=False)
