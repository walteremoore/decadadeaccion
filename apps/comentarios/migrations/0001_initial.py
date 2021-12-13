# Generated by Django 4.0 on 2021-12-13 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articulo', models.CharField(blank=True, max_length=255, null=True)),
                ('contenido', models.TextField(blank=True, null=True)),
                ('estado', models.BooleanField(blank=True, null=True)),
                ('autor', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_creacion', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
