# Generated by Django 4.0.1 on 2022-02-14 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hr', '0004_compensationinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Compensationinfo',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
