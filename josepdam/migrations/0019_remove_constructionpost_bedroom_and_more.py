# Generated by Django 5.0.1 on 2024-02-20 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('josepdam', '0018_constructionpost_bedroom_constructionpost_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='constructionpost',
            name='bedroom',
        ),
        migrations.AddField(
            model_name='constructionpost',
            name='details',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
