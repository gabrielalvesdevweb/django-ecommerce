# Generated by Django 4.0.6 on 2022-07-21 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='data_nascimento',
            field=models.DateField(null=True),
        ),
    ]