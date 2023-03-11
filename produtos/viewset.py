from rest_framework import viewsets

from .serializers import ProdutosSerializer, CategoriaSerializer
from .models import Produtos, Categoria

class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer