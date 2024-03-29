from django.shortcuts import redirect, render, HttpResponse
from pedidos.serializers import PedidosSerializer
from produtos.models import Produtos
from django.contrib import messages
from .forms import FormPedido, FormStatusPedido
from .models import Pedidos
from django.db.models import Q
from django.contrib.auth.decorators import login_required


@login_required(login_url="/usuario/login/")
def index(request):
    pedidos = Pedidos.objects.filter(status_de_pagamento='pendente', status_do_pedido='pronto')
    user = request.user
    
    return render(request, 'html/pedidos.html', {'pedidos': pedidos, 'user': user})

    
@login_required(login_url="/usuario/login/")
def pedido_detalhe(request, pk):
    pedido_detalhe = Pedidos.objects.get(pk=pk)
    list_pedidos = pedido_detalhe.pedidos.all()
    # print(pedido_detalhe.status_de_pagamento[0:].capitalize())
    
    if request.method == "POST":
        form = FormPedido(request.POST, instance=pedido_detalhe)
        if form.is_valid():
            form.save()
            return redirect(F'/pedidos-detalhe/{pk}')
    else:
        form = FormPedido()
    return render(request, 'html/pedido-detalhe.html', { 'pedido_detalhe': pedido_detalhe, 'form': form, 'list_pedidos': list_pedidos })



def historico_de_pedidos(request):
    all_pedidos = Pedidos.objects.filter(status_de_pagamento='pago')
    return render(request, 'html/historico-de-pedidos.html', {'all_pedidos': all_pedidos})




def pedidos_da_cozinha(request):
    return render(request, 'html/pedidos-da-cozinha.html')



def pedido_cozinha_detalhe(request, pk):
    pedido = Pedidos.objects.get(pk=pk)
    list_pedidos = pedido.pedidos.all()
    if request.method == "POST":
        form = FormStatusPedido(request.POST, instance=pedido)
        
        if form.is_valid():
            form.save()
            if form.data['status_do_pedido'] == 'pronto':
                return redirect('pedidos-cozinha')
            else:
                messages.success(request, 'PEDIDO ALTERADO COM SUCESSO!')
            # return redirect(f'pedidos-detalhe-cozinha/{pk}')
        else:
            # Adicionar mensagem de erro
            messages.error(request, 'Erro ao enviar informações')
    else:
        form = FormStatusPedido(instance=pedido)
    return render(request, 'html/detalhe-pedido-cozinha.html', {'pedido': pedido, 'form': form, 'list_pedidos':list_pedidos})

