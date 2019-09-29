from django.urls import path
from .views import listar_produtos, criar_produto, alterar_produto, deletar_produto

urlpatterns = [
    path('', listar_produtos, name='listar_produtos'),
    path('novo', criar_produto, name='criar_produto'),
    path('alterar/<int:id>/', alterar_produto, name='alterar_produto'),
    path('deletar/<int:id>/', deletar_produto, name='deletar_produto'),
]
