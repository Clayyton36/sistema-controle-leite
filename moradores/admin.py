from django.contrib import admin
from .models import Morador


@admin.register(Morador)
class MoradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nis', 'telefone', 'ativo', 'data_cadastro')
    search_fields = ('nome', 'nis')
    list_filter = ('ativo',)