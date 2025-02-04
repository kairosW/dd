# Generated by Django 5.0 on 2024-10-18 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=15)),
                ('comuna', models.CharField(max_length=50)),
                ('fecha_solicitud', models.DateField(auto_now_add=True)),
                ('fecha_aceptacion', models.DateField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('ACEPTADA', 'Aceptada'), ('RECHAZADA', 'Rechazada'), ('EXPIRADA', 'Expirada')], default='PENDIENTE', max_length=10)),
            ],
        ),
    ]
