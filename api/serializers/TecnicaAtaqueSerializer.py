
from api.models.TecnicaAtaque import TecnicaAtaque
from rest_framework import serializers
class TecnicaAtaqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = TecnicaAtaque
        fields = '__all__'
