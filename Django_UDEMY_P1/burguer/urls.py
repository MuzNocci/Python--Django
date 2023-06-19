from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('produto/', views.product, name='product'),

]