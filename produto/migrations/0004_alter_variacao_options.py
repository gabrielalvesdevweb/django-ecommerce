# Generated by Django 4.0.6 on 2022-07-21 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_alter_variacao_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='variacao',
            options={'verbose_name': 'Variável', 'verbose_name_plural': 'Variações'},
        ),
    ]
