from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'burguer/home.html')

def product(request):
    return render(request, 'burguer/produto.html')
