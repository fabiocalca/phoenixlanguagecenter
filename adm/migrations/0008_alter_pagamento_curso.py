# Generated by Django 3.2.16 on 2022-12-20 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0007_auto_20221220_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagamento',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adm.curso'),
        ),
    ]
