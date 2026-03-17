from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_moradores, name='lista_moradores'),
    path('novo/', views.cadastrar_morador, name='cadastrar_morador'),
]