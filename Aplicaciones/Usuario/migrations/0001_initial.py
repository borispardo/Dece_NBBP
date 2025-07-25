# Generated by Django 5.2.1 on 2025-07-21 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('rol', models.CharField(choices=[('Psicólogo', 'Psicólogo'), ('Docente', 'Docente'), ('Administrador', 'Administrador'), ('Orientador', 'Orientador')], max_length=20)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('clave', models.CharField(max_length=128)),
            ],
        ),
    ]
