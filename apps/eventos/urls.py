from django.urls import path
from . import views

app_name = 'eventos'

urlpatterns = [
    path('', views.eventos, name='eventos'),
    path('cadastrar_evento/', views.cadastrar_evento, name='cadastrar_evento'),
    path('adicionar_arquivos/<int:evento_id>/', views.adicionar_arquivos, name='adicionar_arquivos'),
]