# Generated by Django 4.0 on 2021-12-14 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=255, null=True)),
                ('contenido', models.TextField(blank=True, null=True)),
                ('estado', models.BooleanField(blank=True, default=True, null=True)),
                ('visibilidad', models.BooleanField(blank=True, default=False, null=True)),
                ('etiquetas', models.CharField(blank=True, max_length=255, null=True)),
                ('imagen', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_publicacion', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'articulos',
            },
        ),
        migrations.CreateModel(
            name='Etiquetas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'etiquetas',
                'ordering': ['nombre'],
            },
        ),
    ]
