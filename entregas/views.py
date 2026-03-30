from django.shortcuts import render, redirect
from django.db.models import Sum
from datetime import datetime
from .models import Entrega
from .forms import EntregaForm


def lista_entregas(request):
    entregas = Entrega.objects.all().order_by('-data_entrega')

    data_filtro = request.GET.get('data')
    total_pessoas = 0
    total_leite = 0

    if data_filtro:
        try:
            data_obj = datetime.strptime(data_filtro, '%Y-%m-%d').date()
            entregas = entregas.filter(data_entrega=data_obj)
        except ValueError:
            pass

    total_pessoas = entregas.count()
    total_leite = entregas.aggregate(Sum('quantidade'))['quantidade__sum'] or 0

    return render(request, 'entregas/lista.html', {
        'entregas': entregas,
        'total_pessoas': total_pessoas,
        'total_leite': total_leite,
        'data_filtro': data_filtro,
    })


def cadastrar_entrega(request):
    if request.method == 'POST':
        form = EntregaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_entregas')
    else:
        form = EntregaForm()

    return render(request, 'entregas/cadastrar.html', {'form': form})