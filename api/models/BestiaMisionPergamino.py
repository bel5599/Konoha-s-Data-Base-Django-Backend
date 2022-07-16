from django.db import models

from api.models.BestiaMitica import BestiaMitica
from api.models.Mision import Mision
from api.models.Pergamino import Pergamino
class BestiaMisionPergamino(models.Model):
    bestia = models.OneToOneField(BestiaMitica, on_delete=models.CASCADE, null=False, primary_key=True)
    mision = models.ForeignKey(Mision, on_delete=models.CASCADE, null=False)
    pergamino = models.ForeignKey(Pergamino, on_delete=models.CASCADE, null=False)
    class Meta:
        unique_together =[ ['bestia','mision','pergamino']]
