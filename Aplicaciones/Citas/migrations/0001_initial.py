# Generated by Django 5.2.1 on 2025-07-20 23:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CasosIntervencion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('profesional', models.CharField(max_length=100)),
                ('observaciones', models.TextField()),
                ('caso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CasosIntervencion.casointervencion')),
            ],
        ),
    ]
