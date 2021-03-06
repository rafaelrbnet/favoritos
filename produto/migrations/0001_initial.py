# Generated by Django 2.2.4 on 2019-09-04 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('preco', models.IntegerField(verbose_name='Preço')),
                ('imagem', models.CharField(max_length=150, verbose_name='Imagem')),
                ('marca', models.CharField(max_length=150, verbose_name='Marca')),
                ('codigo', models.CharField(max_length=150, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150, verbose_name='Titulo')),
                ('avaliacoes', models.FloatField(verbose_name='Média de Avaliações')),
            ],
        ),
    ]
