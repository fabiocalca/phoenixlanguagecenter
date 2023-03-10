# Generated by Django 3.2.16 on 2022-12-08 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=30)),
                ('contrato_ativo', models.BooleanField(default=True)),
                ('usuario_empresa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
