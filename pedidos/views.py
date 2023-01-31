from django.shortcuts import redirect, render, HttpResponse
from .forms import FormPedido
from .models import Pedidos

from django.contrib.auth.decorators import login_required


@login_required(login_url="/usuario/login/")
def index(request):
    pedidos = Pedidos.objects.all().order_by('numero_da_mesa')
    user = request.user
    
    return render(request, 'html/pedidos.html', {'pedidos': pedidos, 'user': user})

    
@login_required
def pedido_detalhe(request, id):
    pedido_detalhe = Pedidos.objects.get(id=id)
    pedidos = ", ".join([str(pe) for pe in pedido_detalhe.pedidos.all()])
    if request.method == "POST":
        form = FormPedido(request.POST, instance=pedido_detalhe)
        if form.is_valid():
            print(form.data)
            form.save()
            return redirect('/pedidos')
    else:
        form = FormPedido()
    return render(request, 'html/pedido-detalhe.html', {'pedidos': pedidos, 'pedido_detalhe': pedido_detalhe, 'form': form})

def historico_de_pedidos(request):
    all_pedidos = Pedidos.objects.filter(status_de_pagamento='pago')
    return render(request, 'html/historico-de-pedidos.html', {'all_pedidos': all_pedidos})