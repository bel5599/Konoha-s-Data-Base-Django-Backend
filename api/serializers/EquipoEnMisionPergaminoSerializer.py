
from api.models.EquipoEnMisionPergamino import EquipoEnMisionPergamino
from rest_framework import serializers
class EquipoEnMisionPergaminoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipoEnMisionPergamino
        fields = '__all__'
