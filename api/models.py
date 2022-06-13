from email.policy import default
from django.db import models
from datetime import date
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
    def __str__(self) -> str:
        return self.title
class Persona(models.Model):
    nombre = models.CharField(max_length=50, default="")
    edad = models.IntegerField(default=12)
    SEX = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('N', 'No se dice')
    )
    sexo = models.CharField(max_length=1,choices=SEX, default='N')
    clan = models.CharField(max_length=50, default='Konoha')
    fecha_nacimiento = models.DateField(default=date(1,1,1))
class Ninja(Persona):
    chakra_max = models.IntegerField(default=0)
    sobrenombre = models.CharField(max_length=50, default="")
class Genin(Ninja):
    fecha_graduacion = models.DateField(default=date(1,1,1))
    valoracion = models.CharField(max_length=200, default="")
class Chunin(Ninja):
    fecha_examen = models.DateField(default=date(1,1,1))
    calificacion_examen = models.CharField(max_length=100, default="")
class Jounin(Ninja):
    fecha_examen = models.DateField(default=date(1,1,1))
    calificacion_examen = models.CharField(max_length=100, default="")
class Tecnica(models.Model):
    nombre = models.CharField(max_length=50, default="")
    elemento = models.CharField(max_length=30, default="")
    es_oculta = models.BooleanField(default=False)
    cantidad_chakra = models.IntegerField(default=0)
class TecnicaAtaque(Tecnica):
    rango_ataque = models.IntegerField(default=0)
class TecnicaCurativa(Tecnica):
    velocidad_curacion = models.IntegerField(default=0)
class NinjaTecnica(models.Model):
    ninja = models.OneToOneField(Ninja, on_delete=models.CASCADE, null=False, primary_key=True)
    tecnica = models.ForeignKey(Tecnica, on_delete=models.CASCADE, null=False)
    class Meta:
        unique_together = [['ninja','tecnica']]
class NinjaMedico(Ninja):
    pass
class BestiaMitica(models.Model):
    nombre = models.CharField(max_length=50, default="")
    tipo = models.CharField(max_length=30, default="")
    invocador = models.ForeignKey(Ninja, on_delete=models.SET_NULL,null=True)
class Equipo(models.Model):
    nombre = models.CharField(max_length=50, default="")
    ninja1 = models.OneToOneField(Ninja, on_delete=models.CASCADE, related_name='exceptuar_ninja_1', null=False, primary_key=True)
    ninja2 = models.ForeignKey(Ninja, on_delete=models.CASCADE, related_name='exceptuar_ninja_2', null=False)
    ninjamedico = models.ForeignKey(NinjaMedico, on_delete=models.CASCADE, null=False)
    class Meta:
        unique_together = [['ninja1','ninja2','ninjamedico']]

class Mision(models.Model):
    cliente = models.CharField(max_length=50, default="")
    pais_cliente = models.CharField(max_length=30, default="")
    rango = models.CharField(max_length=1, default='')
    recompensa = models.IntegerField(default=0)
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
class Pergamino(models.Model):
    fecha_sellado = models.DateField(default=date(1,1,1))
    ninja = models.ForeignKey(Ninja, on_delete=models.CASCADE, null=False)
    tecnica = models.ForeignKey(Tecnica, on_delete=models.CASCADE, null=False)
class EquipoEnMisionPergamino(models.Model):
    equipoenmision = models.OneToOneField(EquipoEnMision, on_delete=models.CASCADE, null=False, primary_key=True)
    pergamino = models.ForeignKey(Pergamino, on_delete=models.CASCADE, null=False)
    class Meta:
        unique_together = [['equipoenmision','pergamino']]
class BestiaMisionPergaminoLlave(models.Model):
    bestia = models.OneToOneField(BestiaMitica, on_delete=models.CASCADE, null=False, primary_key=True)
    mision = models.ForeignKey(Mision, on_delete=models.CASCADE, null=False)
    pergamino = models.ForeignKey(Pergamino, on_delete=models.CASCADE, null=False)
    class Meta:
        unique_together =[ ['bestia','mision','pergamino']]