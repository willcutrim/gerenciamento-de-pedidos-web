from django.urls import path
from .views import cadastro_usuario

urlpatterns = [
    path('cadastrar-usuario', cadastro_usuario, name='cadastrar-usuario'),
]