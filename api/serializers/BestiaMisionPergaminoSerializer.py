
from api.models.BestiaMisionPergamino import BestiaMisionPergamino
from rest_framework import serializers
class BestiaMisionPergaminoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestiaMisionPergamino
        fields = '__all__'
