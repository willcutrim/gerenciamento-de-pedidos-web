from django.shortcuts import render, HttpResponse
from .models import Produtos, Categoria

def index_pro(request):
    categoria = Categoria.objects.filter(id=2)
    
    for p in categoria:
        pass
    produtos = Produtos.objects.filter(categoria=p.pk)
    refrigerante = Produtos.objects.filter(categoria=1)
    sucos = Produtos.objects.filter(categoria=3)

    
    for s in sucos:
       pass
    for pro in produtos:
       pass
    for refri in refrigerante:
        pass
    return render(request, 'html/home.html', {'produtos': produtos, 'refrigerante': refrigerante, 'refri': refri, 'pro': pro, 'sucos': sucos, 's': s})