# Generated by Django 3.2.16 on 2023-01-16 15:33

from django.db import migrations
import sortedm2m.fields
from sortedm2m.operations import AlterSortedManyToManyField

class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_alter_aluno_options'),
        ('adm', '0009_curso_presenca'),
    ]

    operations = [
        AlterSortedManyToManyField(
            model_name='curso',
            name='alunos_do_curso',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, to='usuarios.Aluno'),
        ),
    ]