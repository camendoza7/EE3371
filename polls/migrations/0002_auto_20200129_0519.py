# Generated by Django 3.0.2 on 2020-01-29 05:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 29, 5, 19, 53, 649379)),
        ),
    ]