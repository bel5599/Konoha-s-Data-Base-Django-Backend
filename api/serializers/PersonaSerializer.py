
from rest_framework import serializers
from api.models.Persona import Persona
class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'
