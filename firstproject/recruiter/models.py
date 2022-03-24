from django.db import models
from django.contrib.auth.models import User


class ProspectCandidate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    skills = models.CharField(verbose_name=('effective start date'), max_length=10, blank=True, null=True)

    totalYearsofExp = models.CharField(verbose_name=('effective end date'), max_length=10, blank=True, null=True)

    releventExp = models.CharField(verbose_name=('hire date'), max_length=10, blank=True, null=True)

    noticePeriod = models.CharField(max_length=1, blank=True, null=True)

    mobile = models.CharField(verbose_name=('termination date'), max_length=10, blank=True, null=True)

    currentCompany = models.CharField(verbose_name=('benafit end  date'), max_length=20, blank=True, null=True)

    Currentctc = models.IntegerField(default=False)
    expectedCtc = models.IntegerField(default=False)
    currentLoc = models.CharField(max_length=20, blank=True, null=True)
    preferredLoc = models.CharField(max_length=20, blank=True, null=True)
    lastWorkingDay = models.CharField(max_length=15, blank=True, null=True)

    lastUpdatedDate = models.DateField(verbose_name=('last updated  date'),auto_now=True, null=False)
    lastUpdatedBy = models.CharField(blank=True, max_length=10, null=True)

    def __str__(self):
        return self.use



