# Generated by Django 5.0.1 on 2024-03-08 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('josepdam', '0041_remove_blogpost_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=50)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='constructionpost',
            name='likes',
        ),
        migrations.AddField(
            model_name='constructionpost',
            name='comments',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
