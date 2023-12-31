# Generated by Django 4.2.5 on 2023-09-18 18:44

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0012_rename_advogado_adv_nome_processo_advogado_adverso_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="processo",
            name="advogado_centralizador",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="advogado_credenciado",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="autor_contumaz",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="processo",
            name="cargo",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="cliente",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="comarca",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="condicao_adversa",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="condicao_cliente",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="cpf_cnpj_adversa",
            field=models.CharField(
                max_length=18,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="CPF/CNPJ deve conter apenas números e ter 11 ou 14 dígitos.",
                        regex="^\\d{11,14}$",
                    )
                ],
            ),
        ),
        migrations.AddField(
            model_name="processo",
            name="cpf_cnpj_terceiro_prestador",
            field=models.CharField(
                max_length=18,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="CPF/CNPJ deve conter apenas números e ter 11 ou 14 dígitos.",
                        regex="^\\d{11,14}$",
                    )
                ],
            ),
        ),
        migrations.AddField(
            model_name="processo",
            name="custas_processuais",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name="processo",
            name="data_ajuizamento",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="data_encerramento",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="data_estimada_pagamento",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="data_estimada_prevista",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="data_evento",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="evento",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="exito",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="handle_perito",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="honorarios",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name="processo",
            name="id_benner",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="inss_empresa",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name="processo",
            name="instancia",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="juizo",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="motivo_desligamento",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="motivo_encerramento",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="nome_desdobramento",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="numero",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="observacao",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="orgao",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="parte_adversa",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="perito",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="risco",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="rito",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="situacao",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="tarefas",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="terceiro",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="terceiro_interessado",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="processo",
            name="terceiro_prestador",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="processo",
            name="total_pago",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name="processo",
            name="tribunal",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="uf",
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="ult_desdobramento",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="processo",
            name="valor_risco",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name="processo",
            name="valor_risco_remoto",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="processo",
            name="data_acordo",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
