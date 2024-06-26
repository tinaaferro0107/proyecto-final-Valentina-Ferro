# Generated by Django 5.0.2 on 2024-03-28 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_personajes_delete_paciente'),
    ]

    operations = [
        migrations.CreateModel(
            name='historias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('resumen', models.CharField(max_length=100)),
                ('protagonistas', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='mundos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('habitantes', models.CharField(max_length=40)),
                ('descripcion', models.EmailField(max_length=100)),
                ('imagen', models.ImageField(upload_to='mundos')),
            ],
        ),
        migrations.CreateModel(
            name='objetos_magicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('descripción', models.CharField(max_length=40)),
                ('dueño', models.CharField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='medico',
        ),
        migrations.DeleteModel(
            name='obra_social',
        ),
        migrations.DeleteModel(
            name='recetas',
        ),
    ]
