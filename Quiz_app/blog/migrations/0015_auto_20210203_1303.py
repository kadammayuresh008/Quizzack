# Generated by Django 3.1.1 on 2021-02-03 07:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20210202_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='Quiz_cover',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='attempts',
            name='attemptedtime',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 3, 13, 3, 7, 869500)),
        ),
    ]
