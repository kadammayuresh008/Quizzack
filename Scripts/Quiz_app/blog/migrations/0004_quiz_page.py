# Generated by Django 3.0.5 on 2020-04-24 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200423_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='quiz_page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(choices=[('option1', 'quiz.option1'), ('option2', 'quiz.option2'), ('option3', 'quiz.option3'), ('option4', 'quiz.option4')], max_length=100)),
            ],
        ),
    ]
