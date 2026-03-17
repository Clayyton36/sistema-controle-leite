from django.db import models
from moradores.models import Morador


class Entrega(models.Model):
    morador = models.ForeignKey(Morador, on_delete=models.CASCADE)
    data_entrega = models.DateField()
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.morador.nome} - {self.data_entrega}"