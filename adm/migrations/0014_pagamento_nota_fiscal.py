# Generated by Django 3.2.16 on 2023-01-19 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0013_curso_aulas_pagas'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagamento',
            name='nota_fiscal',
            field=models.BooleanField(default=False),
        ),
    ]
