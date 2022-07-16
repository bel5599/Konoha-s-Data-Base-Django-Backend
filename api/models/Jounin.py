from django.db import models
from datetime import date
from api.models.Ninja import Ninja
class Jounin(Ninja):
    fecha_examen = models.DateField(default=date(1,1,1))
    calificacion_examen = models.CharField(max_length=100, default="")
