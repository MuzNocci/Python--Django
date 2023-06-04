from django.http import HttpResponse
from django.shortcuts import render


def cadastro(request):
    
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    
    elif request.method == 'POST':
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        dados = f'{username} - {email}'
        
        return HttpResponse(dados)


def login(request):
    return render(request, 'login.html')
