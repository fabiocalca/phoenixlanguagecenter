# Generated by Django 3.2.16 on 2022-12-20 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0006_auto_20221210_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='aulas_dadas',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='curso',
            name='aulas_restantes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pagamento',
            name='aulas_no_pacote',
            field=models.IntegerField(default=0),
        ),
    ]
