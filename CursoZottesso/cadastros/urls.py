from django.urls import path
from .views import CampoCreate, AtividadeCreate, CampoUpdate, AtividadeUpdate, CampoDelete, AtividadeDelete, AtividadeList, CampoList

urlpatterns = [
    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastrar-campo'),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name='cadastrar-atividade'),
    
    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name='editar-campo'),
    path('editar/atividade/<int:pk>/', AtividadeUpdate.as_view(), name='editar-atividade'),

    path('deletar/campo/<int:pk>/', CampoDelete.as_view(), name='deletar-campo'),
    path('deletar/atividade/<int:pk>/', AtividadeDelete.as_view(), name='deletar-atividade'),

    path('listar/campo/', CampoList.as_view(), name='listar-campos'),
    path('listar/atividade/', AtividadeList.as_view(), name='listar-atividades'),
]