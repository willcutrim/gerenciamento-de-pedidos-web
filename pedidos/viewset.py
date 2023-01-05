from rest_framework import viewsets

from .serializers import ProdutosSerializer
from .models import Pedidos

class PedidosViewSet(viewsets.ModelViewSet):
    queryset = Pedidos.objects.all()
    serializer_class = ProdutosSerializer