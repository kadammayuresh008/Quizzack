# Generated by Django 3.1.1 on 2021-02-02 07:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210202_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempts',
            name='attemptedtime',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 2, 12, 48, 47, 855405)),
        ),
    ]