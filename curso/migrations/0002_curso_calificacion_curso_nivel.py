# Generated by Django 5.0.6 on 2024-06-17 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='calificacion',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='curso',
            name='nivel',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]