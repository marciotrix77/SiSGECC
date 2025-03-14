from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required  # Importe o decorator
from .forms import EventoForm, ArquivoForm
from .models import Evento

# Create your views here.
@login_required
def eventos(request):
    return render(request, 'eventos/pages/eventos.html')


@login_required
def cadastrar_evento(request):
    if request.method == 'POST':
        evento_form = EventoForm(request.POST)
        if evento_form.is_valid():
            evento = evento_form.save(commit=False)  # Não salva o evento ainda
            
            # Obtém o objeto Campus do banco de dados usando o ID fornecido no formulário
            campus_id = request.POST.get('campus_responsavel')  # Obtém o ID do campus do request
            campus = Campus.objects.get(pk=campus_id)  # Obtém o objeto Campus do banco de dados
            
            evento.campus_responsavel = campus  # Atribui o objeto Campus ao campo campus_responsavel
            evento.save()  # Agora salva o evento
            
            return redirect('eventos:adicionar_arquivos', evento_id=evento.id)  # Redireciona para a página de adicionar arquivos
    else:
        evento_form = EventoForm()
    return render(request, 'eventos/pages/cadastrar_evento.html', {'evento_form': evento_form})

def adicionar_arquivos(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    if request.method == 'POST':
        arquivo_form = ArquivoForm(request.POST, request.FILES)
        if arquivo_form.is_valid():
            arquivo = arquivo_form.save(commit=False)
            arquivo.evento = evento
            arquivo.save()
            return redirect('eventos:eventos')  # Redireciona para a página de adicionar arquivos
    else:
        arquivo_form = ArquivoForm()
    return render(request, 'eventos/pages/adicionar_arquivos.html', {'arquivo_form': arquivo_form, 'evento': evento})