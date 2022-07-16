from django.db import models
from api.models.Tecnica import Tecnica
class TecnicaCurativa(Tecnica):
    velocidad_curacion = models.IntegerField(default=0)
