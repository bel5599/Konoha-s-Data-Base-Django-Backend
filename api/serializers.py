from rest_framework import serializers
from .models import BestiaMisionPergaminoLlave, BestiaMitica, Chunin, Equipo, EquipoEnMision, EquipoEnMisionPergamino, Genin, Jounin, Mision, Ninja, NinjaMedico, NinjaTecnica, Pergamino, Persona, Task, Tecnica, TecnicaAtaque, TecnicaCurativa

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'
class NinjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ninja
        fields = '__all__'
class GeninSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genin
        fields = '__all__'
class ChuninSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chunin
        fields = '__all__'
class JouninSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jounin
        fields = '__all__'
class TecnicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnica
        fields = '__all__'
class TecnicaAtaqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = TecnicaAtaque
        fields = '__all__'
class TecnicaCurativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TecnicaCurativa
        fields = '__all__'
class NinjaTecnicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NinjaTecnica
        fields = '__all__'
class NinjaMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NinjaMedico
        fields = '__all__'
class BestiaMiticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestiaMitica
        fields = '__all__'
class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'
class MisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mision
        fields = '__all__'
class EquipoEnMisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipoEnMision
        fields = '__all__'
class PergaminoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pergamino
        fields = '__all__'
class EquipoEnMisionPergaminoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipoEnMisionPergamino
        fields = '__all__'
class BestiaMisionPergaminoLlaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestiaMisionPergaminoLlave
        fields = '__all__'