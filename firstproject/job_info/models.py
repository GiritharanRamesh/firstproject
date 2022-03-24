from django.db import models

class JobInfoTable(models.Model):
    person_id = models.CharField(db_column='Person_id', primary_key=True, max_length=10)  # Field name made lowercase.
    job_name = models.CharField(max_length=10, blank=True, null=True)
    employee_class = models.CharField(db_column='Employee_class', max_length=10, blank=True, null=True)  # Field name made lowercase.
    employee_type = models.CharField(db_column='Employee_type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    employee_status = models.CharField(db_column='Employee_status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    job_start_date = models.DateField(db_column='Job_start_date', blank=True, null=True)  # Field name made lowercase.
    position_start_date = models.DateField(db_column='Position_start_date', blank=True, null=True)  # Field name made lowercase.
    is_fulltime_employee = models.IntegerField(blank=True, null=True)
    job_title = models.CharField(db_column='Job_title', max_length=10, blank=True, null=True)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=10, blank=True, null=True)  # Field name made lowercase.
    position_name = models.CharField(db_column='Position_name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    standard_hours = models.CharField(db_column='Standard_hours', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cost_center = models.CharField(db_column='Cost_center', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cost_center_name = models.CharField(db_column='Cost_center_name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    client_based_hire_date = models.DateField(db_column='Client_based_hire_date', blank=True, null=True)  # Field name made lowercase.
    destination = models.CharField(db_column='Destination', max_length=10, blank=True, null=True)  # Field name made lowercase.
