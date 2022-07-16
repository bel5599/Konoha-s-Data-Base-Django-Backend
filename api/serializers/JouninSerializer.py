
from api.models.Jounin import Jounin
from rest_framework import serializers
class JouninSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jounin
        fields = '__all__'
