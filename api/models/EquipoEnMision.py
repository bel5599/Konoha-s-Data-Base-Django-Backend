from django.db import models
from datetime import date
from api.models.Equipo import Equipo
from api.models.Mision import Mision
from api.models.Jounin import Jounin
class EquipoEnMision(models.Model):
    equipo = models.OneToOneField(Equipo, on_delete=models.CASCADE, null=False, primary_key=True)
    mision = models.ForeignKey(Mision, on_delete=models.CASCADE, null=False)
    fecha_inicio = models.DateField(default=date(1,1,1))
    fecha_fin = models.DateField(default=date(1,1,1))
    RESULT = (
        ('S','Satisfactorio'),
        ('NS', 'No Satisfactorio'),
        ('P', 'Pendiente')
    )
    resultado = models.CharField(max_length=20,choices=RESULT, default='P')
    cantidad_shurikens = models.IntegerField(default=0)
    cantidad_kunais = models.IntegerField(default=0)
    cantidad_sellos = models.IntegerField(default=0)
    capitan = models.ForeignKey(Jounin, on_delete=models.CASCADE, null=False)
    class Meta:
        unique_together = [['equipo','mision']]
