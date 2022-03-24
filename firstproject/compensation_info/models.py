from django.db import models

# Create your models here.
class CompensationInfoTable(models.Model):
    currency = models.CharField(db_column='Currency', max_length=10, blank=True, null=True)  # Field name made lowercase.
    basic = models.IntegerField(db_column='Basic', blank=True, null=True)  # Field name made lowercase.
    dearness_allowance = models.IntegerField(db_column='Dearness_allowance', blank=True, null=True)  # Field name made lowercase.
    hra = models.IntegerField(db_column='HRA', blank=True, null=True)  # Field name made lowercase.
    conveyance_allowance = models.IntegerField(db_column='Conveyance_allowance', blank=True, null=True)  # Field name made lowercase.
    special_allowance = models.IntegerField(db_column='Special_allowance', blank=True, null=True)  # Field name made lowercase.
    salary_advance = models.IntegerField(db_column='Salary_advance', blank=True, null=True)  # Field name made lowercase.
    pf_employee = models.IntegerField(db_column='PF_employee', blank=True, null=True)  # Field name made lowercase.
    esic_employee = models.IntegerField(db_column='ESIC_employee', blank=True, null=True)  # Field name made lowercase.
    pt = models.IntegerField(db_column='PT', blank=True, null=True)  # Field name made lowercase.
    pf_employer_cont = models.IntegerField(db_column='PF_employer_cont', blank=True, null=True)  # Field name made lowercase.
    esic_employer_cont = models.IntegerField(db_column='ESIC_employer_cont', blank=True, null=True)  # Field name made lowercase.
    is_effective = models.IntegerField(blank=True, null=True)
    effective_start_date = models.DateField(db_column='Effective_start_date', blank=True, null=True)  # Field name made lowercase.
    effective_end_date = models.DateField(db_column='Effective_end_date', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_updated_by = models.CharField(db_column='Last_updated_by', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_updated_date = models.DateField(db_column='Last_updated_date', blank=True, null=True)  # Field name made lowercase.
