# Generated by Django 4.2.7 on 2025-06-10 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_alter_products_options_products_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='products',
            name='quantlity',
        ),
        migrations.AddField(
            model_name='products',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество'),
        ),
    ]
