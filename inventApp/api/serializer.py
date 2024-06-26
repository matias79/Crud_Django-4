from rest_framework import serializers
from inventApp.models import Proudcto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proudcto
        fields = '__all__'