from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_entregas, name='lista_entregas'),
    path('novo/', views.cadastrar_entrega, name='cadastrar_entrega'),
]