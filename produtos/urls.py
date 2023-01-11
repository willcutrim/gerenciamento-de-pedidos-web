from django.urls import path
from produtos.views import index_pro
from rest_framework_simplejwt.views import TokenVerifyView

from .apiGetController import ProdutosGet, ProdutoDetail

urlpatterns = [
    path('', index_pro, name='index_pro'),
    path('api-produtos/', ProdutosGet.as_view(), name='api-produtos'),

    path('produto-detail/<int:id>', ProdutoDetail.as_view(), name='produto-detail'),


    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
