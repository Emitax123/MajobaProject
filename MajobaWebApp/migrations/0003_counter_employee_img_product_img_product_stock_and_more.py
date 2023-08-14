# Generated by Django 4.1.7 on 2023-05-20 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MajobaWebApp', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='img',
            field=models.ImageField(null=True, upload_to='empleados'),
        ),
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(null=True, upload_to='', verbose_name='Imagen'),
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0, verbose_name='Stock'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MajobaWebApp.category', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, verbose_name='NOmbre'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Precio'),
        ),
    ]