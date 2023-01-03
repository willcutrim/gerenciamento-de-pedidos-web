from django.urls import path
from pedidos.views import index

urlpatterns = [
    path('', index, name='index'),
]
