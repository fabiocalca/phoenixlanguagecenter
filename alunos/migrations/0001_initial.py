# Generated by Django 3.2.16 on 2022-12-08 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('empresa_vinculada', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='empresas.empresa')),
                ('usuario_aluno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
