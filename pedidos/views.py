from django.shortcuts import redirect, render, HttpResponse
from pedidos.serializers import PedidosSerializer
from produtos.models import Produtos
from .forms import FormPedido
from .models import Pedidos
from usuario.models import AvatarUser
from django.contrib.auth.decorators import login_required


@login_required(login_url="/usuario/login/")
def index(request):
    pedidos = Pedidos.objects.filter(status_de_pagamento='pendente')
    user = request.user
    for i in pedidos:
        print(i.numero_da_mesa)
    # if AvatarUser.avatar:
    #     print('ta sem imagem')
    #     avatar = 'C:\\Users\\willyam cutrim\\gerenciamento_de_pedidos\\media\\Image\\user_default.jpg'

    # else:
    avatar = AvatarUser.objects.get(pk=user.pk)
    # avatar = 'Image\\user_default.jpg'

    return render(request, 'html/pedidos.html', {'pedidos': pedidos, 'user': user, 'avatar': avatar})

    
@login_required(login_url="/usuario/login/")
def pedido_detalhe(request, pk):
    pedido_detalhe = Pedidos.objects.get(pk=pk)

    # for i in pedido_detalhe:
    #     pedidos = ", ".join([str(pe) for pe in i.pedidos.all()])
    
    if request.method == "POST":
        form = FormPedido(request.POST, instance=pedido_detalhe)
        if form.is_valid():
            form.save()
            return redirect(F'/pedidos-detalhe/{pk}')
    else:
        form = FormPedido()
    return render(request, 'html/pedido-detalhe.html', { 'pedido_detalhe': pedido_detalhe, 'form': form, })

def historico_de_pedidos(request):
    all_pedidos = Pedidos.objects.filter(status_de_pagamento='pago')
    return render(request, 'html/historico-de-pedidos.html', {'all_pedidos': all_pedidos})



