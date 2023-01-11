from django.shortcuts import render
from .models import Produtos, Categoria
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required


@login_required(login_url="/usuario/login/")
def index_pro(request):
    categoria = Categoria.objects.filter(id=2)
    user = request.user
    for p in categoria:
        pass
    produtos = Produtos.objects.filter(categoria=p.pk)
    refrigerante = Produtos.objects.filter(categoria=1)
    sucos = Produtos.objects.filter(categoria=3)

    for suco, pro, refri in zip(sucos, produtos, refrigerante):
        categoria_suco = suco.categoria
        categoria_produto = pro.categoria
        categoria_refrigerante = refri.categoria

    context = {
        'produtos': produtos, 
        'refrigerante': refrigerante, 
        'categoria_refrigerante': categoria_refrigerante, 
        'categoria_produto': categoria_produto, 
        'sucos': sucos, 
        'categoria_suco': categoria_suco,
        'user': user
    }

    return render(request, 'html/home.html', context)