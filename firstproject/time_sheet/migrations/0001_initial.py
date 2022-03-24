# Generated by Django 4.0.1 on 2022-02-09 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSheetInfoTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_start_date', models.DateField(blank=True, db_column='Week_start_date', null=True)),
                ('monday', models.CharField(blank=True, db_column='Monday', max_length=10, null=True)),
                ('sunday', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]