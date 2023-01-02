from django.urls import path
from produtos.views import index_pro

urlpatterns = [
    path('', index_pro, name='index_pro'),
]
