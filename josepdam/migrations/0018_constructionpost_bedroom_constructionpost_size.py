# Generated by Django 5.0.1 on 2024-02-19 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('josepdam', '0017_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='constructionpost',
            name='bedroom',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='constructionpost',
            name='size',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
