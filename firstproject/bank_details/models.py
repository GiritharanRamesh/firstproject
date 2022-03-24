from django.db import models

class BankDetailsTable(models.Model):
    bank_name = models.CharField(db_column='Bank_name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=10, blank=True, null=True)  # Field name made lowercase.
    account_number = models.CharField(db_column='Account_number', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ifsc_code = models.CharField(db_column='IFSC_code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    beneficiary_name = models.CharField(db_column='Beneficiary_name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    account_type = models.CharField(db_column='Account_type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    routing_number = models.CharField(db_column='Routing_number', max_length=10, blank=True, null=True)