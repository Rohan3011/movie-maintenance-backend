# Generated by Django 4.0.4 on 2022-04-20 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(upload_to='movies_thumbnails'),
        ),
    ]
