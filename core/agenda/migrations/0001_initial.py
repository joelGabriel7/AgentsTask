# Generated by Django 4.1.1 on 2022-09-15 04:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150, verbose_name='Descripcion')),
                ('time_limits', models.DateTimeField(default=datetime.datetime(2022, 9, 14, 23, 22, 30, 231416), verbose_name='Fecha de entrega')),
            ],
        ),
    ]