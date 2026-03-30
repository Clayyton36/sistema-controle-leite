from django.db import models

class Morador(models.Model):
    nome = models.CharField(max_length=100)
    nis = models.CharField(max_length=20, unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=200)
    data_cadastro = models.DateField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} - {self.nis}"