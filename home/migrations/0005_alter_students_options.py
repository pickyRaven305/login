# Generated by Django 4.0.2 on 2022-03-03 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_staff'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='students',
            options={'permissions': (('Student', 'Student'),)},
        ),
    ]
