# Generated by Django 3.2.16 on 2022-12-08 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_empresa_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='usuario_empresa',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='usuario_professor',
        ),
        migrations.DeleteModel(
            name='Aluno',
        ),
        migrations.DeleteModel(
            name='Empresa',
        ),
        migrations.DeleteModel(
            name='Professor',
        ),
    ]
