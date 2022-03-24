from django.db import models

class NationalInfoTable(models.Model):
    national_id = models.CharField(db_column='National_id', max_length=10, blank=True, null=True)  # Field name made lowercase.
    card_type = models.CharField(db_column='Card_type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_updated_by = models.CharField(db_column='Last_updated_by', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_updated_date = models.DateField(db_column='Last_updated_date', blank=True, null=True)  # Field name made lowercase.
