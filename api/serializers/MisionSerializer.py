
from api.models.Mision import Mision
from rest_framework import serializers
class MisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mision
        fields = '__all__'
