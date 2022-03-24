from django.db import models


class QualificationTable(models.Model):
    class_field = models.CharField(db_column='Class', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    mark_percentage = models.IntegerField(db_column='Mark_percentage', blank=True, null=True)  # Field name made lowercase.
    pass_out_year = models.CharField(db_column='Pass_out_year', max_length=10, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=10, blank=True, null=True)  # Field name made lowercase.
    institution_name = models.CharField(db_column='Institution_name', max_length=10, blank=True, null=True)  # Field name made lowercase.
