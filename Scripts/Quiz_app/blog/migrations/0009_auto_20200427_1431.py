# Generated by Django 3.0.5 on 2020-04-27 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_catogaries'),
    ]

    operations = [
        migrations.DeleteModel(
            name='catogaries',
        ),
        migrations.AddField(
            model_name='quiz',
            name='catogaries',
            field=models.CharField(default='', max_length=100),
        ),
    ]
