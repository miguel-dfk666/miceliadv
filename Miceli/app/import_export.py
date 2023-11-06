from import_export import resources
from .models import Processo

class ProcessoResource(resources.ModelResource):
    class Meta:
        model = Processo
        fields = (
           'advogado_nome'
           'advogado_oab'
           'numero_processo'
           'status'
           'assunto'
           'foro'
           'vara'
           'juiz'
           'distribuicao'
           'numero_controle'
           'area'
           'valor_acao'
           'outros_assuntos'
           'patrono'
           'reu'
           'instituicao'
           'documento'
           'julgo_procedente'
           'julgo_improcedente'
           'dano_moral'
           'dano_material'
        )

    skip_unchanged = True
    report_skipped = False
    import_id_fields = ['numero_processo']
