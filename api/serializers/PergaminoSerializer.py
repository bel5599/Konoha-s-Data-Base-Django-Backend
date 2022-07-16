
from api.models.Pergamino import Pergamino
from rest_framework import serializers
class PergaminoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pergamino
        fields = '__all__'
