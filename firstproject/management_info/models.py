from django.db import models

class ManagementInfoTable(models.Model):
    manager_emp_id = models.CharField(db_column='Manager_emp_id', max_length=10, blank=True, null=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    work_phone = models.CharField(db_column='Work_phone', max_length=10, blank=True, null=True)  # Field name made lowercase.
    manager_email = models.CharField(db_column='Manager_email', max_length=10, blank=True, null=True)  # Field name made lowercase.
    is_effective = models.IntegerField(blank=True, null=True)
    effective_start_date = models.DateField(db_column='Effective_start_date', blank=True, null=True)  # Field name made lowercase.
    effective_end_date = models.DateField(db_column='Effective_end_date', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_updated_by = models.CharField(db_column='Last_updated_by', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_updated_date = models.DateField(db_column='Last_updated_date', blank=True, null=True)  # Field name made lowercase.