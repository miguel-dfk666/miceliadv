import datetime
from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

class Processo(models.Model):
    # Processo
    numero_processo = models.CharField(max_length=20, unique=True, null=True)
    descricao = models.TextField(null=True)
    data_cadastro = models.DateField(default=timezone.now)
    juiz_responsavel = models.CharField(max_length=100)
    coligacao = models.CharField(max_length=100, null=True)
    numero_dossie = models.CharField(max_length=25, null=True)
    tipo_de_acao = models.CharField(max_length=100, null=True)
    obj_padrao = models.CharField(max_length=100, null=True)

    # # Autor do processo
    # autor_nome = models.CharField(max_length=100, null=True)
    

    # Réu
    # reu_nome = models.CharField(max_length=100, null=True)

    
    # Advogado Adverso
    advogado_adverso = models.CharField(max_length=100, null=True)
    advogado_agressor = models.CharField(max_length=5, null=True)
    advogado_adverso_numero_oab = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{4,6}/\w+$',
                message='O número da OAB deve estar no formato correto (XXXX/UF). Exemplo: 1234/AB.',
            ),
        ],
        unique=True,
        null=True
    )

    # Advogado Colaborador
    advogado_colaborador = models.CharField(max_length=100, null=True)
    advogado_colaborador_numero_oab = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{4,6}/\w+$',
                message='O número da OAB deve estar no formato correto (XXXX/UF). Exemplo: 1234/AB.',
            ),
        ],
        unique=True,
        null=True
    )
    
    # Sentenca
    tipo_sentenca = models.CharField(max_length=65, null=True)
    data_sentenca = models.DateField(default=timezone.now)
    descricao_sentenca = models.TextField(null=True)
    
    # Acordo
    tipo_acordo = models.CharField(max_length=65, null=True)
    data_acordo = models.DateField(default=timezone.now)
    descricao_acordo = models.TextField(null=True)
    valor_estimado = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    valor_causa = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    valor_pedido = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    valor_risco_provavel = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    data_atualizacao = models.DateTimeField(default=timezone.now, editable=True)


    def save(self, *args, **kwargs):
        self.valor_estimado = round(self.valor_estimado, 2)
        self.valor_causa = round(self.valor_causa, 2)
        self.valor_pedido = round(self.valor_pedido, 2)
        self.valor_risco_provavel = round(self.valor_risco_provavel, 2)

        self.data_atualizacao = timezone.now()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.numero_processo
