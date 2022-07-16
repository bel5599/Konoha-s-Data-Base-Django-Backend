
from api.models.Chunin import Chunin
from rest_framework import serializers
class ChuninSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chunin
        fields = '__all__'
