from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

# Create your models here.
class Processo(models.Model):
  numero_processo = models.CharField(max_length=20, unique=True)
  descricao = models.TextField()
  data_abertura = models.DateField()
  juiz_responsavel = models.CharField(max_length=100)

  def __str__(self):
      return self.numero_processo

class Reu(models.Model):
  nome = models.CharField(max_length=100)
  cpf = models.CharField(max_length=14, unique=True)  # Considere usar um campo CharField para o CPF
  data_nascimento = models.DateField()
  endereco = models.TextField()
  processo = models.ForeignKey('Processo', on_delete=models.CASCADE)  # Relação com o modelo de Processo

  def __str__(self):
      return self.nome
  
class Advogado(models.Model):
    nome = models.CharField(max_length=100)
    numero_oab = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{4,6}/\w+$',
                message='O número da OAB deve estar no formato correto (XXXX/UF). Exemplo: 1234/AB.',
            ),
        ],
        unique=True,  # Se desejar que cada número de OAB seja único
    )

    def __str__(self):
        return self.nome

class Sentenca(models.Model):
  processo = models.ForeignKey('Processo', on_delete=models.CASCADE)
  data_sentenca = models.DateField()
  descricao_sentenca = models.TextField()

  def __str__(self):
      return f"Sentença para o Processo {self.processo.numero_processo}"
    
class Acordo(models.Model):
  processo = models.ForeignKey('Processo', on_delete=models.CASCADE)
  data_acordo = models.DateField()
  descricao_acordo = models.TextField()
  valor_acordo = models.DecimalField(max_digits=10, decimal_places=2)
  data_atualizacao = models.DateTimeField(default=timezone.now, editable=False)

  def save(self, *args, **kwargs):
      self.data_atualizacao = timezone.now()
      super().save(*args, **kwargs)

  def __str__(self):
      return f"Acordo para o Processo {self.processo.numero_processo}"

  def __str__(self):
      return f"Acordo para o Processo {self.processo.numero_processo}"