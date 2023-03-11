from django.urls import path
from pedidos.apiGetControllerPedidos import PedidosList, PedidoCreate
from pedidos.views import index, pedido_detalhe, historico_de_pedidos

urlpatterns = [
    path('', index, name='index'),
    path('pedidos-detalhe/<int:pk>', pedido_detalhe, name='pedidos-detalhe'),

    path('api-pedidos/', PedidosList.as_view(), name='api-pedidos'),
    path('pedidos-create/', PedidoCreate.as_view(), name='pedidos-create'),

    path('historico-de-pedidos/', historico_de_pedidos, name='historico-de-pedidos')
]
