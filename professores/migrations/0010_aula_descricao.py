# Generated by Django 3.2.16 on 2022-12-31 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professores', '0009_aula_professor'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='descricao',
            field=models.TextField(default='Descricao', max_length=500, verbose_name='Descrição'),
        ),
    ]
