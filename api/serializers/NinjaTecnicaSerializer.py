
from api.models.NinjaTecnica import NinjaTecnica
from rest_framework import serializers
class NinjaTecnicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NinjaTecnica
        fields = '__all__'
