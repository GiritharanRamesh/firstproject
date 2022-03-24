from django.db import models

class EmployeeTable(models.Model):
    emp_id = models.CharField(db_column='EmpId', primary_key=True, max_length=10)  # Field name made lowercase.
    effective_start_date = models.DateField(db_column='EffectiveStartDate', blank=True, null=True)  # Field name made lowercase.
    effective_end_date = models.DateField(db_column='EffectiveEndDate', blank=True, null=True)  # Field name made lowercase.
    last_updated_by = models.CharField(db_column='LastUpdatedBy', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_updated_date = models.DateField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.
    hire_date = models.DateField(db_column='HireDate', blank=True, null=True)  # Field name made lowercase.
    ok_to_rehire = models.CharField(db_column='OkToRehire', max_length=10, blank=True, null=True)  # Field name made lowercase.
    termination_date = models.DateField(db_column='TerminationDate', blank=True, null=True)  # Field name made lowercase.
    benefits_start_date = models.DateField(db_column='BenefitsStartDate', blank=True, null=True)  # Field name made lowercase.
    benefits_end_date = models.DateField(db_column='BenefitsEndDate', blank=True, null=True)  # Field name made lowercase.
    is_effective = models.IntegerField(db_column='IsEffective', blank=True, null=True)
    total_years_of_experience = models.CharField(db_column='TotalYearsOfExperience', max_length=10, blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=10, blank=True, null=True)  # Field name made lowercase.
