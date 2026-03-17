from django.contrib import admin
from .models import Morador


@admin.register(Morador)
class MoradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone', 'ativo', 'data_cadastro')
    search_fields = ('nome', 'cpf')
    list_filter = ('ativo',)