from django.urls import path
from .views import cadastro_usuario, login, logout

urlpatterns = [
    path('cadastrar-usuario', cadastro_usuario, name='cadastrar-usuario'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),

]