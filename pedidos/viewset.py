from rest_framework import viewsets

from .serializers import PedidosSerializer
from .models import Pedidos

class PedidosViewSet(viewsets.ModelViewSet):
    serializer_class = PedidosSerializer
    queryset = Pedidos.objects.all()