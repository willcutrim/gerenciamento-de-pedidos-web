from django.shortcuts import render, HttpResponse

from .models import Pedidos


def index(request):
    pedido = Pedidos.objects.filter(status_de_pagamento='pendente')
    
    # pee = Pedidos.objects.get(pk=1)
    # pee = ", ".join([str(pe) for pe in pee.pedidos.all()])
    # print(pee)
    return render(request, 'html/pedidos.html', {'pedidos': pedido})