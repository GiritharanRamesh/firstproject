from django.db import models


class TimeSheetInfoTable(models.Model):
    week_start_date = models.DateField(db_column='Week_start_date', blank=True, null=True)  # Field name made lowercase.
    monday = models.CharField(db_column='Monday', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sunday = models.CharField(max_length=10, blank=True, null=True)
