from django.shortcuts import render, redirect
from .models import Entrega
from .forms import EntregaForm


def lista_entregas(request):
    entregas = Entrega.objects.all()
    return render(request, 'entregas/lista.html', {'entregas': entregas})


def cadastrar_entrega(request):
    if request.method == 'POST':
        form = EntregaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_entregas')
    else:
        form = EntregaForm()

    return render(request, 'entregas/cadastrar.html', {'form': form})
