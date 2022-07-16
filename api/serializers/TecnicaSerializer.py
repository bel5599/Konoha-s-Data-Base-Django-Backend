
from api.models.Tecnica import Tecnica
from rest_framework import serializers
class TecnicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnica
        fields = '__all__'
