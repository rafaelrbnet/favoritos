from django.db import models


class Produto(models.Model):
    preco = models.IntegerField('Preço')
    imagem = models.CharField('Imagem', max_length=150)
    marca = models.CharField('Marca', max_length=150)
    codigo = models.CharField('ID', max_length=150, primary_key=True)
    titulo = models.CharField('Titulo', max_length=150)
    avaliacoes = models.FloatField('Média de Avaliações')

    def __str__(self):
        return self.titulo
