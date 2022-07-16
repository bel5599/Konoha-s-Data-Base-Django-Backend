from django.db import models

from api.models.Tecnica import Tecnica
class TecnicaAtaque(Tecnica):
    rango_ataque = models.IntegerField(default=0)
