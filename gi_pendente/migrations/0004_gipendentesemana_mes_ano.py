# Generated by Django 5.2.3 on 2025-07-05 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gi_pendente', '0003_gipendentesemana_valor_realizado'),
    ]

    operations = [
        migrations.AddField(
            model_name='gipendentesemana',
            name='mes_ano',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
