# Generated by Django 3.2.16 on 2022-12-20 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0008_alter_pagamento_curso'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='presenca',
            field=models.IntegerField(default=0),
        ),
    ]
