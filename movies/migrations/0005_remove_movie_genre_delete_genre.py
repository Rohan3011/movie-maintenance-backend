# Generated by Django 4.0.4 on 2022-04-23 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movie_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]