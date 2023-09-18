from import_export import resources
from .models import Processo

class ProcessoResource(resources.ModelResource):
    class Meta:
        model = Processo
        fields = (
            'numero_processo',
            'data_cadastro',
            'coligacao',
            'numero_dossie',
            'tipo_de_acao',
            'obj_padrao',
            'advogado_adverso',
            'advogado_agressor',
            'advogado_colaborador',
            'valor_estimado',
            'valor_causa',
            'valor_pedido',
            'valor_risco_provavel',
        )

    skip_unchanged = True
    report_skipped = False
    import_id_fields = ['numero_processo']
