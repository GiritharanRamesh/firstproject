from django.db import models

class ContactTable(models.Model):
    phone_no = models.CharField(db_column='Phone_no', max_length=10, blank=True, null=True)  # Field name made lowercase.
    phone_type = models.CharField(db_column='Phone_type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country_code = models.CharField(db_column='Country_code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    extension = models.CharField(db_column='Extension', max_length=10, blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_updated_by = models.CharField(db_column='Last_updated_by', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_updated_date = models.DateField(db_column='Last_updated_date', blank=True, null=True)  # Field name made lowercase.
    address_type = models.CharField(db_column='Address_type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=10, blank=True, null=True)  # Field name made lowercase.
    postal_code = models.CharField(db_column='Postal_code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=10, blank=True, null=True)  # Field name made lowercase.
    is_effective = models.IntegerField(blank=True, null=True)
    effective_start_date = models.DateField(db_column='Effective_start_date', blank=True, null=True)  # Field name made lowercase.
    effective_end_date = models.DateField(db_column='Effective_end_date', blank=True, null=True)  # Field name made lowercase.
