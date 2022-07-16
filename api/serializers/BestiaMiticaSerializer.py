
from api.models.BestiaMitica import BestiaMitica
from rest_framework import serializers
class BestiaMiticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestiaMitica
        fields = '__all__'
