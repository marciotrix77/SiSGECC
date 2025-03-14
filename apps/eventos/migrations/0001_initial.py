# Generated by Django 5.1.7 on 2025-03-13 17:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome do Campus')),
                ('sigla', models.CharField(blank=True, max_length=10, null=True, verbose_name='Sigla do Campus')),
            ],
        ),
        migrations.CreateModel(
            name='TipoEvento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome do Tipo de Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_evento', models.CharField(max_length=255, verbose_name='Nome do Evento')),
                ('descricao_evento', models.TextField(verbose_name='Descrição do Evento')),
                ('data_inicio_evento', models.DateField(verbose_name='Data Início do Evento')),
                ('data_termino_evento', models.DateField(verbose_name='Data Término do Evento')),
                ('campus_responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.campus', verbose_name='Campus Responsável pelo Evento')),
                ('servidor_responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Servidor Responsável pelo Evento')),
                ('tipo_evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.tipoevento', verbose_name='Tipo do Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.FileField(upload_to='eventos/arquivos/', verbose_name='Arquivo')),
                ('nome_original', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome Original do Arquivo')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.evento', verbose_name='Evento')),
            ],
        ),
    ]
