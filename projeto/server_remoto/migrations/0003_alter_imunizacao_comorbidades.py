# Generated by Django 3.2.5 on 2021-07-14 12:19

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server_remoto', '0002_alter_imunizacao_comorbidades'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imunizacao',
            name='comorbidades',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default=None, max_length=30, verbose_name='Comorbidades'), size=None),
        ),
    ]
