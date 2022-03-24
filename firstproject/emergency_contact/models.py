from django.db import models

class EmergencyTable(models.Model):
    primary_flag = models.CharField(db_column='Primary_flag', max_length=10, blank=True, null=True)  # Field name made lowercase.
    relationship = models.CharField(db_column='Relationship', max_length=10, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=10, blank=True, null=True)
    action = models.CharField(db_column='Action', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_updated_by = models.CharField(db_column='Last_updated_by', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_updated_date = models.DateField(db_column='Last_updated_date', blank=True, null=True)  # Field name made lowercase.
