
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from produtos.models import Produtos
from produtos.serializers import ProdutosSerializer

api_view(['GET'])
class ProdutosGet(APIView):
    def get(self, request):
        produtos = Produtos.objects.all()
        serializer = ProdutosSerializer(produtos, many=True)
        return Response(serializer.data)