# Generated by Django 3.2.16 on 2022-12-07 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20221207_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='nome',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
