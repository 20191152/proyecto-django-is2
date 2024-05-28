# Generated by Django 5.0.6 on 2024-05-28 01:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profesor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesor.profesor')),
            ],
        ),
    ]
