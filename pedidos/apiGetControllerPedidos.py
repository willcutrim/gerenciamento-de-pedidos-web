from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from pedidos.models import Pedidos
from pedidos.serializers import PedidosSerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

class PedidosList(APIView):
    
    def get(self, request):
        pedidos = Pedidos.objects.filter(Q(status_do_pedido='pendente') | Q(status_do_pedido='preparando'))
        serializer = PedidosSerializer(pedidos, many=True)
        return Response(serializer.data)

class PedidoCreate(APIView):
    def post(self, request):
        serializer = PedidosSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)