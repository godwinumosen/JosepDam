# Generated by Django 5.0.1 on 2024-03-05 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('josepdam', '0040_alter_constructionpost_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='price',
        ),
    ]