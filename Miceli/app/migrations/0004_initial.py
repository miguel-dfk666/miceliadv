# Generated by Django 4.2.5 on 2023-09-12 15:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("app", "0003_delete_usuario"),
    ]

    operations = [
        migrations.CreateModel(
            name="Advogado",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                (
                    "numero_oab",
                    models.CharField(
                        max_length=10,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="O número da OAB deve estar no formato correto (XXXX/UF). Exemplo: 1234/AB.",
                                regex="^\\d{4,6}/\\w+$",
                            )
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Processo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("numero_processo", models.CharField(max_length=20, unique=True)),
                ("descricao", models.TextField()),
                ("data_abertura", models.DateField()),
                ("juiz_responsavel", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Sentença",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data_sentenca", models.DateField()),
                ("descricao_sentenca", models.TextField()),
                (
                    "processo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.processo"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Reu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("cpf", models.CharField(max_length=14, unique=True)),
                ("data_nascimento", models.DateField()),
                ("endereco", models.TextField()),
                (
                    "processo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.processo"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Acordo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data_acordo", models.DateField()),
                ("descricao_acordo", models.TextField()),
                ("valor_acordo", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "data_atualizacao",
                    models.DateTimeField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "processo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.processo"
                    ),
                ),
            ],
        ),
    ]