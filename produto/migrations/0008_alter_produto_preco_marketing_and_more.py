# Generated by Django 4.0.6 on 2022-07-22 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0007_alter_produto_preco_marketing_promocional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco_marketing',
            field=models.FloatField(verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_marketing_promocional',
            field=models.FloatField(default=0, verbose_name='Preço Promo'),
        ),
    ]
