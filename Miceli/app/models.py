import datetime
from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

class Processo(models.Model):
    # Processo
    numero_processo = models.CharField(max_length=20, unique=True, null=True)
    descricao = models.TextField(default=timezone.now)
    data_cadastro = models.DateField(null=True)
    juiz_responsavel = models.CharField(max_length=100)
    coligacao = models.CharField(max_length=100, null=True)

    # Autor do processo
    autor_nome = models.CharField(max_length=100, null=True)
    autor_cpf = models.CharField(max_length=14, unique=True, null=True)
    autor_data_nascimento = models.DateField(default=timezone.now)
    autor_endereco = models.TextField(null=True)

    # Réu
    reu_nome = models.CharField(max_length=100, null=True)
    reu_cpf = models.CharField(max_length=14, unique=True, null=True)
    reu_data_nascimento = models.DateField(default=timezone.now)
    reu_endereco = models.TextField(null=True)
    
    # Advogado
    advogado_nome = models.CharField(max_length=100, null=True)
    advogado_cpf = models.CharField(max_length=14, unique=True, null=True)
    advogado_data_nascimento = models.DateField(default=timezone.now)
    advogado_endereco = models.TextField(null=True)
    advogado_numero_oab = models.CharField(
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
    data_acordo = models.DateField(default=timezone.now())
    descricao_acordo = models.TextField(null=True)
    valor_estimado = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    valor_causa = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    valor_pedido = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    valor_risco_provavel = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    data_atualizacao = models.DateTimeField(default=timezone.now, editable=True)

    def save(self, *args, **kwargs):
        self.data_atualizacao = timezone.now()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.numero_processo
