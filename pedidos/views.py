from django.shortcuts import redirect, render, HttpResponse
from produtos.models import Produtos
from .forms import FormPedido
from .models import Pedidos
from usuario.models import AvatarUser
from django.contrib.auth.decorators import login_required


@login_required(login_url="/usuario/login/")
def index(request):
    pedidos = Pedidos.objects.filter(status_de_pagamento='pendente')
    for i in pedidos:

        mesa = Pedidos.objects.get(nome_do_cliente=i.nome_do_cliente)
    mesas = mesa.numero_da_mesa.all()
    print(mesas)
    user = request.user
    
    # if AvatarUser.avatar:
    #     print('ta sem imagem')
    #     avatar = 'C:\\Users\\willyam cutrim\\gerenciamento_de_pedidos\\media\\Image\\user_default.jpg'

    # else:
    avatar = AvatarUser.objects.get(pk=user.pk)
    # avatar = 'Image\\user_default.jpg'

    return render(request, 'html/pedidos.html', {'pedidos': pedidos, 'user': user, 'avatar': avatar})

    
@login_required(login_url="/usuario/login/")
def pedido_detalhe(request, pk):
    pedido_detalhe = Pedidos.objects.filter(pk=pk)

    for i in pedido_detalhe:
        pedidos = ", ".join([str(pe) for pe in i.pedidos.all()])
        numero_da_mesa = ", ".join([str(pe) for pe in i.numero_da_mesa.all()])
    print(numero_da_mesa)
    pedidos_form = Pedidos.objects.get(pk=i.pk)
    if request.method == "POST":
        form = FormPedido(request.POST, instance=pedidos_form)
        if form.is_valid():
            form.save()
            return redirect(F'/pedidos-detalhe/{pk}')
    else:
        form = FormPedido()
    return render(request, 'html/pedido-detalhe.html', { 'pedido_detalhe': pedido_detalhe, 'form': form, 'pedidos': pedidos})

def historico_de_pedidos(request):
    all_pedidos = Pedidos.objects.filter(status_de_pagamento='pago')
    return render(request, 'html/historico-de-pedidos.html', {'all_pedidos': all_pedidos})



