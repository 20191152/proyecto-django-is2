# Generated by Django 5.0.6 on 2024-06-07 13:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estudiante', '0001_initial'),
        ('profesor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=250)),
                ('categoria', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('ultima_modificacion', models.DateField(auto_now=True)),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesor.profesor')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_matricula', models.DateTimeField(auto_now_add=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curso.curso')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiante.estudiante')),
            ],
        ),
    ]
