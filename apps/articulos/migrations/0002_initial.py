# Generated by Django 4.0 on 2021-12-13 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
        ('articulos', '0001_initial'),
        ('categorias', '0001_initial'),
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
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='categorias.categoria'),
        ),
    ]
