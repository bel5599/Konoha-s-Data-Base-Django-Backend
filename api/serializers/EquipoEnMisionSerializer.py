
from api.models.EquipoEnMision import EquipoEnMision
from rest_framework import serializers
class EquipoEnMisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipoEnMision
        fields = '__all__'
