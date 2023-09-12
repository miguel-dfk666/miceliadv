from django.contrib import admin
from .models import Reu, Processo, Sentenca, Acordo, Advogado  # Importe seus modelos aqui

# Registre os modelos no administrador
admin.site.register(Advogado)
admin.site.register(Reu)
admin.site.register(Processo)
admin.site.register(Sentenca)
admin.site.register(Acordo)
