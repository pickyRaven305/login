# Generated by Django 4.0.2 on 2022-03-01 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_sessionyear_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='password',
            field=models.CharField(max_length=16),
        ),
    ]
