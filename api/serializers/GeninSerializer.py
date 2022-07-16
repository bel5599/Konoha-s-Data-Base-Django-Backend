
from api.models.Genin import Genin
from rest_framework import serializers
class GeninSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genin
        fields = '__all__'
