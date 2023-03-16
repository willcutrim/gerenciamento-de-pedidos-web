from django.urls import path
from pedidos.apiGetControllerPedidos import PedidosList, PedidoCreate
from pedidos.views import index, pedido_detalhe, historico_de_pedidos, pedidos_da_cozinha, pedido_cozinha_detalhe

urlpatterns = [
    path('', index, name='index'),
    path('pedidos-detalhe/<int:pk>', pedido_detalhe, name='pedidos-detalhe'),
    path('pedidos-cozinha/', pedidos_da_cozinha, name='pedidos-cozinha'),
    path('pedidos-detalhe-cozinha/<int:pk>', pedido_cozinha_detalhe, name='pedidos-detalhe-cozinha'),

    path('api-pedidos/', PedidosList.as_view(), name='api-pedidos'),
    path('pedidos-create/', PedidoCreate.as_view(), name='pedidos-create'),

    path('historico-de-pedidos/', historico_de_pedidos, name='historico-de-pedidos')
]
