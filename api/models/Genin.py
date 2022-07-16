from django.db import models
from datetime import date
from api.models.Ninja import Ninja
class Genin(Ninja):
    fecha_graduacion = models.DateField(default=date(1,1,1))
    valoracion = models.CharField(max_length=200, default="")

