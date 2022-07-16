
from api.models.Equipo import Equipo
from rest_framework import serializers
class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'
