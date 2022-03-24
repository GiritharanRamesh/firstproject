# Generated by Django 4.0.1 on 2022-02-07 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobInfoTable',
            fields=[
                ('person_id', models.CharField(db_column='Person_id', max_length=10, primary_key=True, serialize=False)),
                ('job_name', models.CharField(blank=True, max_length=10, null=True)),
                ('employee_class', models.CharField(blank=True, db_column='Employee_class', max_length=10, null=True)),
                ('employee_type', models.CharField(blank=True, db_column='Employee_type', max_length=10, null=True)),
                ('employee_status', models.CharField(blank=True, db_column='Employee_status', max_length=10, null=True)),
                ('job_start_date', models.DateField(blank=True, db_column='Job_start_date', null=True)),
                ('position_start_date', models.DateField(blank=True, db_column='Position_start_date', null=True)),
                ('is_fulltime_employee', models.IntegerField(blank=True, null=True)),
                ('job_title', models.CharField(blank=True, db_column='Job_title', max_length=10, null=True)),
                ('position', models.CharField(blank=True, db_column='Position', max_length=10, null=True)),
                ('position_name', models.CharField(blank=True, db_column='Position_name', max_length=10, null=True)),
                ('standard_hours', models.CharField(blank=True, db_column='Standard_hours', max_length=10, null=True)),
                ('cost_center', models.CharField(blank=True, db_column='Cost_center', max_length=10, null=True)),
                ('cost_center_name', models.CharField(blank=True, db_column='Cost_center_name', max_length=10, null=True)),
                ('client_based_hire_date', models.DateField(blank=True, db_column='Client_based_hire_date', null=True)),
                ('destination', models.CharField(blank=True, db_column='Destination', max_length=10, null=True)),
            ],
        ),
    ]
