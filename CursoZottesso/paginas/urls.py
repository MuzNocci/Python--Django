from django.urls import path
from .views import IndexView, AboutView, ShopView, ContactView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('contact/', ContactView.as_view(), name='contact'),
]