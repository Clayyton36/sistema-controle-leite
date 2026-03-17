from django.contrib import admin
from .models import Entrega


@admin.register(Entrega)
class EntregaAdmin(admin.ModelAdmin):
    list_display = ('morador', 'data_entrega', 'quantidade')
    search_fields = ('morador__nome', 'morador__cpf')
    list_filter = ('data_entrega',)
