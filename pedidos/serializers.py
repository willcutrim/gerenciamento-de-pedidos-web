from rest_framework import serializers
from .models import Pedidos

class PedidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedidos
        fields = '__all__'