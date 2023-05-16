from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ShopView(TemplateView):
    template_name = 'shop.html'

class ContactView(TemplateView):
    template_name = 'contact.html'