
from api.models.NinjaMedico import NinjaMedico
from rest_framework import serializers
class NinjaMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NinjaMedico
        fields = '__all__'
