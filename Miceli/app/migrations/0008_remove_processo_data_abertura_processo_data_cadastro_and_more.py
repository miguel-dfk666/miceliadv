# Generated by Django 4.2.4 on 2023-09-14 14:51

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_reu_processo_remove_sentenca_processo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processo',
            name='data_abertura',
        ),
        migrations.AddField(
            model_name='processo',
            name='data_cadastro',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='processo',
            name='data_acordo',
            field=models.DateField(default=datetime.datetime(2023, 9, 14, 14, 51, 2, 468606, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='processo',
            name='descricao',
            field=models.TextField(default=django.utils.timezone.now),
        ),
    ]