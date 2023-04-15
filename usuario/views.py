from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout as logout_django, login as login_django
from django.contrib import messages
from .forms import CadastroForm


@login_required(login_url="/usuario/login/")
def cadastro_usuario(request):
    
    if request.method == 'POST':
        form = CadastroForm(request.POST or None)
        try:
            usuario_exists = User.objects.get(email=request.POST.get('email'))
            if usuario_exists:
                messages.warning(request, 'Este e-mail já está sendo utilizado!')
                
        except User.DoesNotExist:
            if form.is_valid():
                username = request.POST.get('username')
                email = request.POST.get('email')
                password = request.POST.get('password')

                novo_usuario = User.objects.create_user(username=username, email=email, password=password)
                novo_usuario.save()
                
                messages.success(request, 'Usuário criado com sucesso!')
    else: 
        form = CadastroForm()
    return render(request, 'html/cadastro_usuario.html', {'form': form})


@login_required(login_url="/usuario/login/")
def user_list(request):
    users = User.objects.filter(is_superuser=False)
    return render(request, 'html/user_list.html', {'users': users})



def login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        url = request.GET.get('next')
        if user:
            login_django(request, user)
            if url != None:
                return redirect(url)
            else:
                return redirect('/')
            
        else:
            return HttpResponse('email ou senha invalida')
    return render(request, 'html/login.html')



def logout(request):
    if request.user.is_authenticated:
        logout_django(request)
        return HttpResponseRedirect('/usuario/login/')
