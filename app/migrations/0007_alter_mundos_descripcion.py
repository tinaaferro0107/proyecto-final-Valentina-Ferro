# Generated by Django 5.0.2 on 2024-03-28 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_historias_mundos_objetos_magicos_delete_medico_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mundos',
            name='descripcion',
            field=models.CharField(max_length=100),
        ),
    ]