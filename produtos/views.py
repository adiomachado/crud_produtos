from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})


def criar_produto(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_produtos')

    return render(request, 'produtos-form.html', {'form': form})


def alterar_produto(request, id):
    produto = Produto.objects.get(id=id)
    form = ProdutoForm(request.POST or None, instance=produto)
    isdelete = True

    if form.is_valid():
        form.save()
        return redirect('listar_produtos')

    return render(request, 'produtos-form.html', {'form': form, 'produto': produto})


def deletar_produto(request, id):
    produto = Produto.objects.get(id=id)

    if request.method == 'POST':
        produto.delete()
        return redirect('listar_produtos')

    return render(request, 'produto-deletar-confirmar.html', {'produto': produto})
