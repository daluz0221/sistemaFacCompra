# Generated by Django 3.2.8 on 2021-10-10 19:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inv', '0002_subcategoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creado')),
                ('fm', models.DateTimeField(auto_now=True, verbose_name='fecha modificado')),
                ('um', models.PositiveIntegerField(blank=True, null=True)),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Empresa productora')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Productoras',
            },
        ),
    ]
