from django.db import models

class ExperienceTable(models.Model):
    previous_org_name = models.CharField(db_column='Previous_org_name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    start_period = models.CharField(db_column='Start_period', max_length=10, blank=True, null=True)  # Field name made lowercase.
    end_period = models.CharField(db_column='End_period', max_length=10, blank=True, null=True)  # Field name made lowercase.
    years_of_experience = models.IntegerField(blank=True, null=True)
    reference_name = models.CharField(db_column='Reference_name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    reference_contact = models.CharField(db_column='Reference_contact', max_length=10, blank=True, null=True)  # Field name made lowercase.
