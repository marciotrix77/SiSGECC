from django.contrib.auth.models import AbstractUser
from django.db import models

class Campus(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome do Campus")
    sigla = models.CharField(max_length=10, verbose_name="Sigla do Campus", blank=True, null=True)

    def __str__(self):
        return self.nome

class User(AbstractUser):
    nome_completo = models.CharField(max_length=255, verbose_name="Nome Completo")
    campus_lotacao = models.ForeignKey(Campus, on_delete=models.CASCADE, verbose_name="Campus de Lotação")
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")
    matricula = models.CharField(max_length=20, unique=True, verbose_name="Matrícula")
    cargo = models.CharField(max_length=255, verbose_name="Cargo")
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="login_user_set",
        related_query_name="login_user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="login_user_set",
        related_query_name="login_user",
    )

    def __str__(self):
        return self.username