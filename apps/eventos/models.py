from django.db import models
from django.conf import settings  # Importe as configurações para acessar o modelo User

class TipoEvento(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome do Tipo de Evento")

    def __str__(self):
        return self.nome

class Campus(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome do Campus")
    sigla = models.CharField(max_length=10, verbose_name="Sigla do Campus", blank=True, null=True)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    nome_evento = models.CharField(max_length=255, verbose_name="Nome do Evento")
    tipo_evento = models.ForeignKey(TipoEvento, on_delete=models.CASCADE, verbose_name="Tipo do Evento")
    descricao_evento = models.TextField(verbose_name="Descrição do Evento")
    campus_responsavel = models.ForeignKey(Campus, on_delete=models.CASCADE, verbose_name="Campus Responsável pelo Evento")
    servidor_responsavel = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Servidor Responsável pelo Evento",
    )
    data_inicio_evento = models.DateField(verbose_name="Data Início do Evento")
    data_termino_evento = models.DateField(verbose_name="Data Término do Evento")

    def __str__(self):
        return self.nome_evento
    
class Arquivo(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, verbose_name="Evento")
    arquivo = models.FileField(upload_to='eventos/arquivos/', verbose_name="Arquivo")
    nome_original = models.CharField(max_length=255, verbose_name="Nome Original do Arquivo", blank=True, null=True)

    def __str__(self):
        return self.nome_original or self.arquivo.name