from rest_framework import viewsets

from .serializers import ProdutosSerializer
from .models import Produtos

class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer