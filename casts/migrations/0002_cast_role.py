# Generated by Django 4.0.4 on 2022-04-19 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cast',
            name='role',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
