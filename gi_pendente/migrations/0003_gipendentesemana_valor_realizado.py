# Generated by Django 5.2.3 on 2025-07-05 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gi_pendente', '0002_gipendentesemana_delete_gipendente'),
    ]

    operations = [
        migrations.AddField(
            model_name='gipendentesemana',
            name='valor_realizado',
            field=models.FloatField(default=0),
        ),
    ]
