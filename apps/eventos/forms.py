from django import forms
from eventos.models import Evento, Arquivo, TipoEvento 
from django.contrib.auth.models import User
from eventos.models import Campus


class EventoForm(forms.ModelForm):
    nome_evento = forms.CharField(
        label="Nome do Evento",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do evento'})
    )
    tipo_evento = forms.ModelChoiceField(
        queryset=TipoEvento.objects.all(),  # Substitua TipoEvento pelo seu modelo de tipo de evento
        label="Tipo do Evento",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    descricao_evento = forms.CharField(
        label="Descrição do Evento",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    )
    campus_responsavel = forms.ModelChoiceField(
        queryset=Campus.objects.all(),  # Substitua Campus pelo seu modelo de campus
        label="Campus Responsável",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    servidor_responsavel = forms.ModelChoiceField(
        queryset=User.objects.all(),  # Substitua User pelo seu modelo de usuário
        label="Servidor Responsável",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    data_inicio_evento = forms.DateField(
        label="Data Início do Evento",
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    data_termino_evento = forms.DateField(
        label="Data Término do Evento",
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = Evento
        fields = '__all__'  # Inclui todos os campos do modelo

class ArquivoForm(forms.ModelForm):
    arquivo = forms.FileField(
        label="Arquivo",
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Arquivo
        fields = ['arquivo']        