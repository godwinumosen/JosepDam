# Generated by Django 5.0.1 on 2024-02-27 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('josepdam', '0025_remove_constructionpost_search_delete_search'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board_of_directorpost',
            name='board_of_director_position',
            field=models.CharField(blank=True, max_length=210, null=True),
        ),
    ]
