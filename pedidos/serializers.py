from rest_framework import serializers
from .models import Pedidos

class PedidosSerializer(serializers.ModelSerializer):
    data_do_pedido = serializers.DateTimeField(format="%d/%m/%Y - %H:%M:%S", required=False, read_only=True)
    class Meta:
        model = Pedidos
        fields = '__all__'