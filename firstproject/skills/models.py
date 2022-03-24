from django.db import models

class SkillsTable(models.Model):
    is_primary = models.IntegerField(blank=True, null=True)
    technology = models.CharField(db_column='Technology', max_length=10, blank=True, null=True)  # Field name made lowercase.
    years_of_experience = models.IntegerField(db_column='Years_of_experience', blank=True, null=True)  # Field name made lowercase.
    last_used = models.CharField(db_column='Last_used', max_length=10, blank=True, null=True)  # Field name made lowercase.
    certified = models.IntegerField(db_column='Certified', blank=True, null=True)  # Field name made lowercase.
