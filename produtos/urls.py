from django.urls import path
from produtos.views import index_pro

from .apiGetController import ProdutosGet, ProdutoDetail

urlpatterns = [
    path('', index_pro, name='index_pro'),
    path('api-produtos/', ProdutosGet.as_view(), name='api-produtos'),

    path('produto-detail/<int:id>', ProdutoDetail.as_view(), name='produto-detail'),
]
