from django.shortcuts import render
from django.contrib.auth.models import User
# from django.http import HttpResponseRedirect
# from django.contrib.auth import authenticate, login, logout


def cadastro_usuario(request):
    if request.method == 'POST':
        try:
            usuario_exists = User.objects.get(email=request.POST.get('email'))
            if usuario_exists:
                return 'usuario ja existe'
        except User.DoesNotExist:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            novo_usuario = User.objects.create_user(username=username, email=email, password=password)

            novo_usuario.save()
            
        
    return render(request, 'html/cadastro_usuario.html')



# @require_POST
# def entrar(request):
#     usuario_aux = User.objects.get(email=request.POST['email'])
#     usuario = authenticate(username=usuario_aux.username,
#                            password=request.POST["senha"])
#     if usuario is not None:
#         login(request, usuario)
#         return HttpResponseRedirect('/home/')

#     return HttpResponseRedirect('/')


# def index(request):
#     if request.user.is_authenticated:
#         return HttpResponseRedirect("/home/")
#     else:
#         return render(request, "caminho para index.html")