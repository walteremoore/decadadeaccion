# Generated by Django 4.0 on 2021-12-14 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articulos', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='categoria',
            field=models.ManyToManyField(to='articulos.Etiquetas'),
        ),
    ]