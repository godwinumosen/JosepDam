# Generated by Django 5.0.1 on 2024-03-01 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('josepdam', '0036_remove_constructionpost_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secondconstruction',
            name='size',
        ),
    ]
