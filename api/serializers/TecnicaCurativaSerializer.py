
from api.models.TecnicaCurativa import TecnicaCurativa
from rest_framework import serializers
class TecnicaCurativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TecnicaCurativa
        fields = '__all__'
