from django.urls import path
from .views import cadastro_usuario, login, logout, user_list

from .api_login import ObterToken

urlpatterns = [
    path('cadastrar-usuario', cadastro_usuario, name='cadastrar-usuario'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),

    path('api-login/', ObterToken.as_view(), name='api-login'),

    path('user-list', user_list, name='user-list')

]