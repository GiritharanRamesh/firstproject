from django.db import models

class OrganizationTable(models.Model):
    organization_type = models.CharField(db_column='Organization_type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=10, blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=10, blank=True, null=True)  # Field name made lowercase.
    company_code = models.CharField(db_column='Company_code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    company_name = models.CharField(db_column='Company_name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    account_code = models.CharField(db_column='Account_code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    account_bt_name = models.CharField(db_column='Account_bt_name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=10, blank=True, null=True)  # Field name made lowercase.
    postal_code = models.CharField(db_column='Postal_code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=10, blank=True, null=True)  # Field name made lowercase.