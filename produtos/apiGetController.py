from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from produtos.models import Produtos, Categoria
from produtos.serializers import ProdutosSerializer, CategoriaSerializer



class ProdutosGet(APIView):
    
    def get(self, request):
        produtos = Produtos.objects.all()
        serializer = ProdutosSerializer(produtos, many=True)
        return Response(serializer.data)

class ProdutosByCategory(APIView):
    
    def get_produto(self, id):
        try:
            return Produtos.objects.get(id=id)
        except Produtos.DoesNotExist:
            raise Http404

    def get(self, request, id):
        produtos = Produtos.objects.filter(categoria=id)
        serializer = ProdutosSerializer(produtos, many=True)
        return Response(serializer.data)

class ProdutoDetail(APIView):
    
    def get_produto(self, id):
        try:
            return Produtos.objects.get(id=id)
        except Produtos.DoesNotExist:
            raise Http404

    def get(self, request, id):
        produto_id = self.get_produto(id)
        serializer = ProdutosSerializer(produto_id)
        return Response(serializer.data)
 
    
class CategoriaGet(APIView):
    def get(self, request):
        produtos = Categoria.objects.all()
        serializer = CategoriaSerializer(produtos, many=True)
        return Response(serializer.data)