from django.urls import path
from pedidos.views import index

urlpatterns = [
    path('pedidos', index, name='index'),
]
