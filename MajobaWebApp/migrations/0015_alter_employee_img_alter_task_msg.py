# Generated by Django 4.1.7 on 2023-07-18 21:50

import MajobaWebApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MajobaWebApp', '0014_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='img',
            field=models.ImageField(default=MajobaWebApp.models.default_image, null=True, upload_to='media/empleados/', verbose_name='Fotografia'),
        ),
        migrations.AlterField(
            model_name='task',
            name='msg',
            field=models.CharField(max_length=50, verbose_name='Indique la tarea a realizar'),
        ),
    ]
