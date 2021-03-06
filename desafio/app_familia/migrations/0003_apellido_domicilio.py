# Generated by Django 4.0.5 on 2022-06-12 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_familia', '0002_familias_delete_familia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apellido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Apellido_or', models.CharField(max_length=40)),
                ('Pais', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=40)),
                ('calle', models.IntegerField()),
                ('viviendo_desde', models.DateField()),
            ],
        ),
    ]
