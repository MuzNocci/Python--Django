from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def cadastro(request):
    
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    
    elif request.method == 'POST':
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('O usuário já existe no banco de dados.')
        
        if not password == confirm_password:
            return HttpResponse('As senhas não conferem.')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return HttpResponse(f'Usuário {username.upper()}, cadastrado com sucesso.')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = hash(request.POST.get('password'))

        user = authenticate(username=username, password=password)

        if user:
            login_django(request, user)
            return redirect(dashboard)
        else:
            return HttpResponse('Usuário ou senhas incorretos')

@login_required(login_url="/auth/login/")     
def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponse('Você não está logado.')
    return HttpResponse(f'Olá {request.user.first_name}! Bem vindo ao Dashboard.')

def logout(request):
    logout_django(request)
    return redirect(login)
