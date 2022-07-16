
from api.models.Ninja import Ninja
from rest_framework import serializers
class NinjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ninja
        fields = '__all__'
