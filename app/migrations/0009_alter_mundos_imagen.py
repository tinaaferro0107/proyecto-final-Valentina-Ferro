# Generated by Django 5.0.2 on 2024-03-28 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_mundos_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mundos',
            name='imagen',
            field=models.ImageField(upload_to='mundos'),
        ),
    ]