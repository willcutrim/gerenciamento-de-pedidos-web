from django.contrib import admin

from produtos.models import Categoria, Produtos
admin.site.register(Categoria)
admin.site.register(Produtos)
