from django.db import models


class LeaveProgressTable(models.Model):
    year = models.CharField(db_column='Year', max_length=10, blank=True, null=True)  # Field name made lowercase.
    leave_balance = models.IntegerField(db_column='Leave_balance', blank=True, null=True)  # Field name made lowercase.
    leaves_availed = models.IntegerField(db_column='Leaves_availed', blank=True, null=True)  # Field name made lowercase.
    emp_id = models.ForeignKey('EmployeeEmployeetable', on_delete=models.RESTRICT, default="E0001")


class EmployeeEmployeetable(models.Model):
    emp_id = models.CharField(db_column='Emp_id', primary_key=True, max_length=10)  # Field name made lowercase.
