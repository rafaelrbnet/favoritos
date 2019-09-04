from django.db import models


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=150)
    email = models.CharField('E-mail', max_length=150, unique=True)

    def __str__(self):
        return self.nome
