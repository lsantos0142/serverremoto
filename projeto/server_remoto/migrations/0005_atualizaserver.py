# Generated by Django 3.2.5 on 2021-07-16 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server_remoto', '0004_alter_imunizacao_comorbidades'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtualizaServer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atualiza', models.BooleanField()),
            ],
        ),
    ]
