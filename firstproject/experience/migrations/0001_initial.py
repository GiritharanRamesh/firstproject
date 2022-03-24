# Generated by Django 4.0.1 on 2022-02-07 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExperienceTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previous_org_name', models.CharField(blank=True, db_column='Previous_org_name', max_length=10, null=True)),
                ('start_period', models.CharField(blank=True, db_column='Start_period', max_length=10, null=True)),
                ('end_period', models.CharField(blank=True, db_column='End_period', max_length=10, null=True)),
                ('years_of_experience', models.IntegerField(blank=True, null=True)),
                ('reference_name', models.CharField(blank=True, db_column='Reference_name', max_length=10, null=True)),
                ('reference_contact', models.CharField(blank=True, db_column='Reference_contact', max_length=10, null=True)),
            ],
        ),
    ]
