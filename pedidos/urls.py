from django.urls import path
from pedidos.apiGetControllerPedidos import PedidosList
from pedidos.views import index, pedido_detalhe

urlpatterns = [
    path('', index, name='index'),
    path('pedidos-detalhe/<int:id>', pedido_detalhe, name='pedidos-detalhe'),

    path('api-pedidos/', PedidosList.as_view(), name='api-pedidos'),

]
