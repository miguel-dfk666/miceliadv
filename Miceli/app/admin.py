from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import ExcelUploadForm
from .models import Processo
import pandas as pd

class ProcessoAdmin(admin.ModelAdmin):
    actions = ['importar_dados_excel']

    def importar_dados_excel(self, request, queryset):
        if 'upload_excel' in request.POST:
            form = ExcelUploadForm(request.POST, request.FILES)
            if form.is_valid():
                arquivo_excel = request.FILES['dados_planilha']
                self.message_user(request, "Dados importados com sucesso")
                return HttpResponseRedirect(reverse('admin:%s_%s_changelist' % (
                    self.model._meta.app_label, self.model._meta.model_name,
                )))
            else:
                form = ExcelUploadForm()
            context = {
                'forms' : form,
                'opts' : self.model_meta,
            }
        return render(request, 'admin/importar_excel.html', context)
    #     try:
    #         df = pd.read_excel(arquivo_excel)
    #         if df.empty:
    #             self.message_user(request, "O arquivo Excel está vazio.", level='error')
    #             return

    #         for index, row in df.iterrows():
    #             processo = Processo(
    #                 numero_processo=row['Número Processo'],
    #                 data_cadastro=row['Data Cadastro'],
    #                 coligacao=row['Coligada'],
    #                 numero_dossie=row['Nº Do Dossiê'],
    #                 tipo_de_acao=row['Tipo De Ação'],
    #                 obj_padrao=row['Objeto Padrão'],
    #                 adovago_adv_nome=row['Adv Adverso'],
    #                 advogado_adv_agressor=row['Adv Agressor'],
    #                 advogado_colaborador_nome=row['Advogado Colaborador'],
    #                 valor_estimado=row['V. Estimado'],
    #                 valor_causa=row['V. Causa'],
    #                 valor_pedido=row['V. Pedido'],
    #                 valor_risco_provavel=row['V.Risco Provavel'],
    #             )
    #             processo.save()
    #         self.message_user(request, "Dados importados com sucesso.")
    #     except Exception as e:
    #         self.message_user(request, f"Erro ao importar dados: {str(e)}", level='error')

    # importar_dados_excel.short_description = "Importar dados do Excel"

admin.site.register(Processo, ProcessoAdmin)
