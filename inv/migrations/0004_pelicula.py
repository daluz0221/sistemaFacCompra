# Generated by Django 3.2.8 on 2021-10-11 05:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inv', '0003_productora'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creado')),
                ('fm', models.DateTimeField(auto_now=True, verbose_name='fecha modificado')),
                ('um', models.PositiveIntegerField(blank=True, null=True)),
                ('codigo', models.CharField(max_length=50, unique=True, verbose_name='Código de pelicula')),
                ('nombre', models.CharField(max_length=80, verbose_name='Nombre de la película')),
                ('descripcion', models.CharField(max_length=500, verbose_name='descripción')),
                ('precio', models.FloatField(default=0)),
                ('existencia', models.PositiveIntegerField(default=1)),
                ('last_buy', models.DateField(blank=True, null=True, verbose_name='Última compra')),
                ('productora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.productora')),
                ('subcategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.subcategoria')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Películas',
                'unique_together': {('codigo',)},
            },
        ),
    ]
