from django.db import models
from cliente.models import Cliente
from produto.models import Produto


class Favoritos(models.Model):
    cliente = models.OneToOneField(
        Cliente,
        verbose_name='Cliente',
        related_name='favoritos',
        on_delete=models.CASCADE,
        unique=True,
        primary_key=True
    )
    produto = models.ManyToManyField(
        Produto, verbose_name='Produtos', related_name='favoritos', blank=True
    )

    def __str__(self):
        return self.cliente.nome
