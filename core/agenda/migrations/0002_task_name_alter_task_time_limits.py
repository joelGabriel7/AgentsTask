# Generated by Django 4.1.1 on 2022-09-15 04:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='name',
            field=models.CharField(default=2, max_length=50, verbose_name='Nombre'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='time_limits',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 14, 23, 26, 32, 318057), verbose_name='Fecha de entrega'),
        ),
    ]
