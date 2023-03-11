from django.urls import path
from produtos.views import index_pro
from rest_framework_simplejwt.views import TokenVerifyView

from .apiGetController import ProdutosGet, ProdutoDetail, ProdutosByCategory, CategoriaGet

urlpatterns = [
    path('', index_pro, name='index_pro'),
    path('api-produtos/', ProdutosGet.as_view(), name='api-produtos'),
    path('api-categoria/', CategoriaGet.as_view(), name='api-categoria'),
    path('api-produtos/bycategoria/<int:id>', ProdutosByCategory.as_view(), name='api-produtos-bycategoria'),

    path('produto-detail/<int:id>', ProdutoDetail.as_view(), name='produto-detail'),


    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
