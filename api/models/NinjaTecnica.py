from django.db import models
from api.models.Ninja import Ninja
from api.models.Tecnica import Tecnica
class NinjaTecnica(models.Model):
    ninja = models.OneToOneField(Ninja, on_delete=models.CASCADE, null=False, primary_key=True)
    tecnica = models.ForeignKey(Tecnica, on_delete=models.CASCADE, null=False)
    class Meta:
        unique_together = [['ninja','tecnica']]
