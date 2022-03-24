from django.db import models


class PersonalInfoTable(models.Model):
    first_name = models.CharField(db_column='First_name', primary_key=True, max_length=10)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    intial = models.CharField(db_column='Intial', max_length=5, blank=True, null=True)  # Field name made lowercase.
    marital_status = models.CharField(db_column='Marital_status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ethnicity_code = models.CharField(db_column='Ethnicity_code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    is_effective = models.IntegerField(blank=True, null=True)
    effective_start_date = models.DateField(db_column='Effective_start_date', blank=True, null=True)  # Field name made lowercase.
    effective_end_date = models.DateField(db_column='Effective_end_date', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_updated_by = models.CharField(db_column='Last_updated_by', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_updated_date = models.DateField(db_column='Last_updated_date', blank=True, null=True)  # Field name made lowercase.
