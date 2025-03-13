from django.contrib import admin
from eventos.models import TipoEvento, Campus, Evento, Arquivo # Importe os modelos

admin.site.register(TipoEvento)
admin.site.register(Campus)
admin.site.register(Evento)
admin.site.register(Arquivo)