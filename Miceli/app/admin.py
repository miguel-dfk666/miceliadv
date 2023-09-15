from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from import_export.admin import ImportExportModelAdmin
from .models import Processo
import pandas as pd


@admin.register(Processo)
class ProcessoAdmin(admin.ModelAdmin):
    list_display = (
        'data_cadastro',
        'valor_estimado',
        'valor_causa',
        'valor_pedido',
        'valor_risco_provavel',
        'numero_processo',
        'advogado_adverso',
        'advogado_agressor',
        'advogado_colaborador',
        'numero_dossie',
        'coligacao',
        'tipo_de_acao',
        'obj_padrao',
    )
