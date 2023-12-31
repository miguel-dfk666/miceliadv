# Generated by Django 4.2.4 on 2023-09-15 02:26

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_processo_data_acordo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processo',
            name='autor_cpf',
        ),
        migrations.RemoveField(
            model_name='processo',
            name='autor_data_nascimento',
        ),
        migrations.RemoveField(
            model_name='processo',
            name='autor_endereco',
        ),
        migrations.RemoveField(
            model_name='processo',
            name='autor_nome',
        ),
        migrations.RemoveField(
            model_name='processo',
            name='reu_cpf',
        ),
        migrations.RemoveField(
            model_name='processo',
            name='reu_data_nascimento',
        ),
        migrations.RemoveField(
            model_name='processo',
            name='reu_endereco',
        ),
        migrations.RemoveField(
            model_name='processo',
            name='reu_nome',
        ),
        migrations.AlterField(
            model_name='processo',
            name='data_acordo',
            field=models.DateField(default=datetime.datetime(2023, 9, 15, 2, 26, 23, 580604, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='processo',
            name='data_cadastro',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='processo',
            name='descricao',
            field=models.TextField(null=True),
        ),
    ]
