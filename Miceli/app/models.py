from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

class Processo(models.Model):
    # Processo
    numero_processo = models.CharField(max_length=20, unique=True)
    descricao = models.TextField()
    data_abertura = models.DateField()
    juiz_responsavel = models.CharField(max_length=100)
    
    # Autor do processo
    autor_nome = models.CharField(max_length=100)
    autor_cpf = models.CharField(max_length=14, unique=True)
    autor_data_nascimento = models.DateField()
    autor_endereco = models.TextField()

    # Réu
    reu_nome = models.CharField(max_length=100)
    reu_cpf = models.CharField(max_length=14, unique=True)
    reu_data_nascimento = models.DateField()
    reu_endereco = models.TextField()
    
    # Advogado
    advogado_nome = models.CharField(max_length=100)
    advogado_cpf = models.CharField(max_length=14, unique=True)
    advogado_numero_oab = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{4,6}/\w+$',
                message='O número da OAB deve estar no formato correto (XXXX/UF). Exemplo: 1234/AB.',
            ),
        ],
        unique=True,
    )
    
    # Sentenca
    tipo_sentenca = models.CharField(max_length=65)
    data_sentenca = models.DateField()
    descricao_sentenca = models.TextField()
    
    # Acordo
    tipo_acordo = models.CharField(max_length=65)
    data_acordo = models.DateField()
    descricao_acordo = models.TextField()
    valor_acordo = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    valor_causa = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    valor_pedido = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    risco_provavel = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    data_atualizacao = models.DateTimeField(default=timezone.now, editable=False)

    def save(self, *args, **kwargs):
        self.data_atualizacao = timezone.now()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.numero_processo
