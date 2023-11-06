import datetime
from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

class Processo(models.Model):
    # Informações Básicas do Processo
    advogado_nome = models.CharField(max_length=100, null=True)
    advogado_oab = models.CharField(max_length=30, null=True)
    numero_processo = models.CharField(max_length=100, null=True)  # Número do Processo
    status = models.CharField(max_length=50, null=True)  # Status do Processo
    assunto = models.CharField(max_length=200, null=True)  # Assunto do Processo
    foro = models.CharField(max_length=100, null=True)  # Foro do Processo
    vara = models.CharField(max_length=100, null=True)  # Vara do Processo
    juiz = models.CharField(max_length=100, null=True)  # Juíz do Processo
    distribuicao = models.DateField(null=True)  # Data de Distribuição do Processo
    numero_controle = models.CharField(max_length=50, null=True)  # Número de Controle do Processo
    area = models.CharField(max_length=100, null=True)  # Área do Processo
    valor_acao = models.CharField(max_length=100, null=True)  # Valor da Ação do Processo
    outros_assuntos = models.TextField(null=True)  # Outros Assuntos relacionados ao Processo
    patrono = models.CharField(max_length=200, null=True)  # Patrono do Processo
    reu = models.CharField(max_length=200, null=True)  # Réu do Processo
    instituicao = models.CharField(max_length=200, null=True)  # Instituição relacionada ao Processo
    documento = models.FileField(upload_to='documentos/', null=True)  # Campo para documentos (PDFs, por exemplo)
    julgo_procedente = models.CharField(max_length=50, null=True)
    julgo_improcedente = models.CharField(max_length=50, null=True)
    dano_moral = models.CharField(max_length=100, null=True)
    dano_material = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.numero_processo
