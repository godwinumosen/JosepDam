# Generated by Django 5.0.1 on 2024-03-08 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('josepdam', '0044_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
