from django.apps import AppConfig
from django.contrib import admin

# from usuario.models import AvatarUser, User

class UsuarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuario'

class AvatarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'avataruser'