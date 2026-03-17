from django.shortcuts import render, redirect
from .models import Morador
from .forms import MoradorForm


def lista_moradores(request):
    moradores = Morador.objects.all()
    return render(request, 'moradores/lista.html', {'moradores': moradores})


def cadastrar_morador(request):
    if request.method == 'POST':
        form = MoradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_moradores')
    else:
        form = MoradorForm()

    return render(request, 'moradores/cadastrar.html', {'form': form})