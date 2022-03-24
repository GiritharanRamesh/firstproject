# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Compensationinfo(models.Model):
    empid = models.ForeignKey('Employee', models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=10, blank=True, null=True)  # Field name made lowercase.
    basic = models.IntegerField(db_column='Basic', blank=True, null=True)  # Field name made lowercase.
    dearnessallowance = models.IntegerField(db_column='DearnessAllowance', blank=True, null=True)  # Field name made lowercase.
    hra = models.IntegerField(db_column='HRA', blank=True, null=True)  # Field name made lowercase.
    conveyanceallowance = models.IntegerField(db_column='ConveyanceAllowance', blank=True, null=True)  # Field name made lowercase.
    specialallowance = models.IntegerField(db_column='SpecialAllowance', blank=True, null=True)  # Field name made lowercase.
    salaryadvance = models.IntegerField(db_column='SalaryAdvance', blank=True, null=True)  # Field name made lowercase.
    pfemployee = models.IntegerField(db_column='PFEmployee', blank=True, null=True)  # Field name made lowercase.
    esicemployee = models.IntegerField(db_column='ESICEmployee', blank=True, null=True)  # Field name made lowercase.
    pt = models.IntegerField(db_column='PT', blank=True, null=True)  # Field name made lowercase.
    pfemployercont = models.IntegerField(db_column='PFEmployerCont', blank=True, null=True)  # Field name made lowercase.
    esicemployercont = models.IntegerField(db_column='ESICEmployerCont', blank=True, null=True)  # Field name made lowercase.
    iseffective = models.IntegerField(db_column='IsEffective', blank=True, null=True)  # Field name made lowercase.
    effectivestartdate = models.DateField(db_column='EffectiveStartDate', blank=True, null=True)  # Field name made lowercase.
    effectiveenddate = models.DateField(db_column='EffectiveEndDate', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.CharField(db_column='LastUpdatedBy', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CompensationInfo'


class Contact(models.Model):
    empid = models.ForeignKey('Employee', models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.
    phoneno = models.CharField(db_column='PhoneNo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    phonetype = models.CharField(db_column='PhoneType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    extension = models.CharField(db_column='Extension', max_length=10, blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.CharField(db_column='LastUpdatedBy', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.
    addresstype = models.CharField(db_column='AddressType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=10, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=10, blank=True, null=True)  # Field name made lowercase.
    iseffective = models.IntegerField(db_column='IsEffective', blank=True, null=True)  # Field name made lowercase.
    effectivestartdate = models.DateField(db_column='EffectiveStartDate', blank=True, null=True)  # Field name made lowercase.
    effectiveenddate = models.DateField(db_column='EffectiveEndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Contact'


class Emergencycontact(models.Model):
    empid = models.ForeignKey('Employee', models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.
    primaryflag = models.CharField(db_column='PrimaryFlag', max_length=10, blank=True, null=True)  # Field name made lowercase.
    relationship = models.CharField(db_column='Relationship', max_length=10, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=10, blank=True, null=True)
    action = models.CharField(db_column='Action', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.CharField(db_column='LastUpdatedBy', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmergencyContact'


class Employee(models.Model):
    empid = models.CharField(db_column='EmpId', primary_key=True, max_length=10)  # Field name made lowercase.
    effectivestartdate = models.DateField(db_column='EffectiveStartDate', blank=True, null=True)  # Field name made lowercase.
    effectiveenddate = models.DateField(db_column='EffectiveEndDate', blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.CharField(db_column='LastUpdatedBy', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.
    hiredate = models.DateField(db_column='HireDate', blank=True, null=True)  # Field name made lowercase.
    oktorehire = models.CharField(db_column='OkToRehire', max_length=10, blank=True, null=True)  # Field name made lowercase.
    terminationdate = models.DateField(db_column='TerminationDate', blank=True, null=True)  # Field name made lowercase.
    benefitsstartdate = models.DateField(db_column='BenefitsStartDate', blank=True, null=True)  # Field name made lowercase.
    benefitsenddate = models.DateField(db_column='BenefitsEndDate', blank=True, null=True)  # Field name made lowercase.
    iseffective = models.IntegerField(db_column='IsEffective', blank=True, null=True)  # Field name made lowercase.
    totalyearsofexperience = models.CharField(db_column='TotalYearsOfExperience', max_length=10, blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Employee'


class Experience(models.Model):
    empid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.
    previousorgname = models.CharField(db_column='PreviousOrgName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    startperiod = models.CharField(db_column='StartPeriod', max_length=10, blank=True, null=True)  # Field name made lowercase.
    endperiod = models.CharField(db_column='EndPeriod', max_length=10, blank=True, null=True)  # Field name made lowercase.
    yearsofexperience = models.IntegerField(db_column='yearsOfExperience', blank=True, null=True)  # Field name made lowercase.
    referencename = models.CharField(db_column='ReferenceName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    referencecontact = models.CharField(db_column='ReferenceContact', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Experience'


class HrCompensationinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    currency = models.CharField(db_column='Currency', max_length=10, blank=True, null=True)  # Field name made lowercase.
    basic = models.IntegerField(db_column='Basic', blank=True, null=True)  # Field name made lowercase.
    dearnessallowance = models.IntegerField(db_column='DearnessAllowance', blank=True, null=True)  # Field name made lowercase.
    hra = models.IntegerField(db_column='HRA', blank=True, null=True)  # Field name made lowercase.
    conveyanceallowance = models.IntegerField(db_column='ConveyanceAllowance', blank=True, null=True)  # Field name made lowercase.
    specialallowance = models.IntegerField(db_column='SpecialAllowance', blank=True, null=True)  # Field name made lowercase.
    salaryadvance = models.IntegerField(db_column='SalaryAdvance', blank=True, null=True)  # Field name made lowercase.
    pfemployee = models.IntegerField(db_column='PFEmployee', blank=True, null=True)  # Field name made lowercase.
    esicemployee = models.IntegerField(db_column='ESICEmployee', blank=True, null=True)  # Field name made lowercase.
    pt = models.IntegerField(db_column='PT', blank=True, null=True)  # Field name made lowercase.
    pfemployercont = models.IntegerField(db_column='PFEmployerCont', blank=True, null=True)  # Field name made lowercase.
    esicemployercont = models.IntegerField(db_column='ESICEmployerCont', blank=True, null=True)  # Field name made lowercase.
    iseffective = models.IntegerField(db_column='IsEffective', blank=True, null=True)  # Field name made lowercase.
    effectivestartdate = models.DateField(db_column='EffectiveStartDate', blank=True, null=True)  # Field name made lowercase.
    effectiveenddate = models.DateField(db_column='EffectiveEndDate', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.CharField(db_column='LastUpdatedBy', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.
    empid = models.ForeignKey('HrEmployee', models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Hr_compensationinfo'


class HrEmployee(models.Model):
    empid = models.CharField(db_column='EmpId', primary_key=True, max_length=10)  # Field name made lowercase.
    effectivestartdate = models.DateField(db_column='EffectiveStartDate', blank=True, null=True)  # Field name made lowercase.
    effectiveenddate = models.DateField(db_column='EffectiveEndDate', blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.CharField(db_column='LastUpdatedBy', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.
    hiredate = models.DateField(db_column='HireDate', blank=True, null=True)  # Field name made lowercase.
    oktorehire = models.CharField(db_column='OkToRehire', max_length=10, blank=True, null=True)  # Field name made lowercase.
    terminationdate = models.DateField(db_column='TerminationDate', blank=True, null=True)  # Field name made lowercase.
    benefitsstartdate = models.DateField(db_column='BenefitsStartDate', blank=True, null=True)  # Field name made lowercase.
    benefitsenddate = models.DateField(db_column='BenefitsEndDate', blank=True, null=True)  # Field name made lowercase.
    iseffective = models.IntegerField(db_column='IsEffective', blank=True, null=True)  # Field name made lowercase.
    totalyearsofexperience = models.CharField(db_column='TotalYearsOfExperience', max_length=10, blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Hr_employee'


class Jobinfo(models.Model):
    empid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.
    personid = models.CharField(db_column='PersonId', primary_key=True, max_length=10)  # Field name made lowercase.
    jobname = models.CharField(db_column='JobName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    employeecclass = models.CharField(db_column='EmployeecClass', max_length=10, blank=True, null=True)  # Field name made lowercase.
    employeetype = models.CharField(db_column='EmployeeType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    employeestatus = models.CharField(db_column='EmployeeStatus', max_length=10, blank=True, null=True)  # Field name made lowercase.
    jobstartdate = models.DateField(db_column='JobStartDate', blank=True, null=True)  # Field name made lowercase.
    positionstartdate = models.DateField(db_column='PositionStartDate', blank=True, null=True)  # Field name made lowercase.
    isfulltimeemployee = models.IntegerField(db_column='IsFulltimeEmployee', blank=True, null=True)  # Field name made lowercase.
    jobtitle = models.CharField(db_column='JobTitle', max_length=10, blank=True, null=True)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=10, blank=True, null=True)  # Field name made lowercase.
    positionname = models.CharField(db_column='PositionName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    standardhours = models.CharField(db_column='StandardHours', max_length=10, blank=True, null=True)  # Field name made lowercase.
    costcenter = models.CharField(db_column='CostCenter', max_length=10, blank=True, null=True)  # Field name made lowercase.
    costcentername = models.CharField(db_column='CostCenterName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    clientbasedhiredate = models.DateField(db_column='ClientBasedHireDate', blank=True, null=True)  # Field name made lowercase.
    destination = models.CharField(db_column='Destination', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JobInfo'


class Leaveinfo(models.Model):
    empid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=10, blank=True, null=True)  # Field name made lowercase.
    leavebalance = models.IntegerField(db_column='LeaveBalance', blank=True, null=True)  # Field name made lowercase.
    leavesavailed = models.IntegerField(db_column='LeavesAvailed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LeaveInfo'


class Managementinfo(models.Model):
    empid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.
    managerempid = models.CharField(db_column='ManagerEmpId', max_length=10, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    workphone = models.CharField(db_column='WorkPhone', max_length=10, blank=True, null=True)  # Field name made lowercase.
    manageremail = models.CharField(db_column='ManagerEmail', max_length=10, blank=True, null=True)  # Field name made lowercase.
    iseffective = models.IntegerField(db_column='IsEffective', blank=True, null=True)  # Field name made lowercase.
    effectivestartdate = models.DateField(db_column='EffectiveStartDate', blank=True, null=True)  # Field name made lowercase.
    effectiveenddate = models.DateField(db_column='EffectiveEndDate', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.CharField(db_column='LastUpdatedBy', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ManagementInfo'


class Nationalinfo(models.Model):
    empid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.
    nationalid = models.CharField(db_column='NationalId', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cardtype = models.CharField(db_column='CardType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.CharField(db_column='LastUpdatedBy', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NationalInfo'


class Organization(models.Model):
    empid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.
    organizationtype = models.CharField(db_column='OrganizationType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=10, blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=10, blank=True, null=True)  # Field name made lowercase.
    companycode = models.CharField(db_column='CompanyCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    accountcode = models.CharField(db_column='AccountCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    accountbtname = models.CharField(db_column='AccountBtName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=10, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Organization'


class Personalinfo(models.Model):
    empid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', primary_key=True, max_length=10)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    intial = models.CharField(db_column='Intial', max_length=5, blank=True, null=True)  # Field name made lowercase.
    maritalstatus = models.CharField(db_column='MaritalStatus', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ethnicitycode = models.CharField(db_column='EthnicityCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    iseffective = models.IntegerField(db_column='IsEffective', blank=True, null=True)  # Field name made lowercase.
    effectivestartdate = models.DateField(db_column='EffectiveStartDate', blank=True, null=True)  # Field name made lowercase.
    effectiveenddate = models.DateField(db_column='EffectiveEndDate', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.CharField(db_column='LastUpdatedBy', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PersonalInfo'


class Qualification(models.Model):
    empid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    markpercentage = models.IntegerField(db_column='MarkPercentage', blank=True, null=True)  # Field name made lowercase.
    passoutyear = models.CharField(db_column='PassOutYear', max_length=10, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=10, blank=True, null=True)  # Field name made lowercase.
    institutionname = models.CharField(db_column='InstitutionName', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Qualification'


class Skills(models.Model):
    empid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.
    isprimary = models.IntegerField(db_column='IsPrimary', blank=True, null=True)  # Field name made lowercase.
    technology = models.CharField(db_column='Technology', max_length=10, blank=True, null=True)  # Field name made lowercase.
    yearsofexperience = models.IntegerField(db_column='YearsOfExperience', blank=True, null=True)  # Field name made lowercase.
    lastused = models.CharField(db_column='LastUsed', max_length=10, blank=True, null=True)  # Field name made lowercase.
    certified = models.IntegerField(db_column='Certified', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Skills'


class Timesheetinfo(models.Model):
    empid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.
    weekstartdate = models.DateField(db_column='WeekStartDate', blank=True, null=True)  # Field name made lowercase.
    monday = models.CharField(db_column='Monday', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sunday = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TimeSheetInfo'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bankdetails(models.Model):
    empid = models.ForeignKey(Employee, models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=10, blank=True, null=True)  # Field name made lowercase.
    accountnumber = models.CharField(db_column='AccountNumber', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ifsccode = models.CharField(db_column='IFSCCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    beneficiaryname = models.CharField(db_column='BeneficiaryName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    accounttype = models.CharField(db_column='AccountType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    routingnumber = models.CharField(db_column='RoutingNumber', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bankDetails'


class BankDetailsBankdetailstable(models.Model):
    id = models.BigAutoField(primary_key=True)
    bank_name = models.CharField(db_column='Bank_name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=10, blank=True, null=True)  # Field name made lowercase.
    account_number = models.CharField(db_column='Account_number', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ifsc_code = models.CharField(db_column='IFSC_code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    beneficiary_name = models.CharField(db_column='Beneficiary_name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    account_type = models.CharField(db_column='Account_type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    routing_number = models.CharField(db_column='Routing_number', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bank_details_bankdetailstable'


class CompensationInfoCompensationinfotable(models.Model):
    id = models.BigAutoField(primary_key=True)
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

    class Meta:
        managed = False
        db_table = 'compensation_info_compensationinfotable'


class ContactContacttable(models.Model):
    id = models.BigAutoField(primary_key=True)
    phone_no = models.CharField(db_column='Phone_no', max_length=10, blank=True, null=True)  # Field name made lowercase.
    phone_type = models.CharField(db_column='Phone_type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country_code = models.CharField(db_column='Country_code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    extension = models.CharField(db_column='Extension', max_length=10, blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_updated_by = models.CharField(db_column='Last_updated_by', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_updated_date = models.DateField(db_column='Last_updated_date', blank=True, null=True)  # Field name made lowercase.
    address_type = models.CharField(db_column='Address_type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=10, blank=True, null=True)  # Field name made lowercase.
    postal_code = models.CharField(db_column='Postal_code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=10, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=10, blank=True, null=True)  # Field name made lowercase.
    is_effective = models.IntegerField(blank=True, null=True)
    effective_start_date = models.DateField(db_column='Effective_start_date', blank=True, null=True)  # Field name made lowercase.
    effective_end_date = models.DateField(db_column='Effective_end_date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contact_contacttable'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EmergencyContactEmergencytable(models.Model):
    id = models.BigAutoField(primary_key=True)
    primary_flag = models.CharField(db_column='Primary_flag', max_length=10, blank=True, null=True)  # Field name made lowercase.
    relationship = models.CharField(db_column='Relationship', max_length=10, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=10, blank=True, null=True)
    action = models.CharField(db_column='Action', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_updated_by = models.CharField(db_column='Last_updated_by', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_updated_date = models.DateField(db_column='Last_updated_date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emergency_contact_emergencytable'


class EmployeeEmployeetable(models.Model):
    empid = models.CharField(db_column='EmpId', primary_key=True, max_length=10)  # Field name made lowercase.
    effectivestartdate = models.DateField(db_column='EffectiveStartDate', blank=True, null=True)  # Field name made lowercase.
    effectiveenddate = models.DateField(db_column='EffectiveEndDate', blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.CharField(db_column='LastUpdatedBy', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.
    hiredate = models.DateField(db_column='HireDate', blank=True, null=True)  # Field name made lowercase.
    oktorehire = models.CharField(db_column='OkToRehire', max_length=10, blank=True, null=True)  # Field name made lowercase.
    terminationdate = models.DateField(db_column='TerminationDate', blank=True, null=True)  # Field name made lowercase.
    benefitsstartdate = models.DateField(db_column='BenefitsStartDate', blank=True, null=True)  # Field name made lowercase.
    benefitsenddate = models.DateField(db_column='BenefitsEndDate', blank=True, null=True)  # Field name made lowercase.
    iseffective = models.IntegerField(db_column='IsEffective', blank=True, null=True)  # Field name made lowercase.
    totalyearsofexperience = models.CharField(db_column='TotalYearsOfExperience', max_length=10, blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee_employeetable'


class ExperienceExperiencetable(models.Model):
    id = models.BigAutoField(primary_key=True)
    previous_org_name = models.CharField(db_column='Previous_org_name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    start_period = models.CharField(db_column='Start_period', max_length=10, blank=True, null=True)  # Field name made lowercase.
    end_period = models.CharField(db_column='End_period', max_length=10, blank=True, null=True)  # Field name made lowercase.
    years_of_experience = models.IntegerField(blank=True, null=True)
    reference_name = models.CharField(db_column='Reference_name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    reference_contact = models.CharField(db_column='Reference_contact', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'experience_experiencetable'


class JobInfoJobinfotable(models.Model):
    person_id = models.CharField(db_column='Person_id', primary_key=True, max_length=10)  # Field name made lowercase.
    job_name = models.CharField(max_length=10, blank=True, null=True)
    employee_class = models.CharField(db_column='Employee_class', max_length=10, blank=True, null=True)  # Field name made lowercase.
    employee_type = models.CharField(db_column='Employee_type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    employee_status = models.CharField(db_column='Employee_status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    job_start_date = models.DateField(db_column='Job_start_date', blank=True, null=True)  # Field name made lowercase.
    position_start_date = models.DateField(db_column='Position_start_date', blank=True, null=True)  # Field name made lowercase.
    is_fulltime_employee = models.IntegerField(blank=True, null=True)
    job_title = models.CharField(db_column='Job_title', max_length=10, blank=True, null=True)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=10, blank=True, null=True)  # Field name made lowercase.
    position_name = models.CharField(db_column='Position_name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    standard_hours = models.CharField(db_column='Standard_hours', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cost_center = models.CharField(db_column='Cost_center', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cost_center_name = models.CharField(db_column='Cost_center_name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    client_based_hire_date = models.DateField(db_column='Client_based_hire_date', blank=True, null=True)  # Field name made lowercase.
    destination = models.CharField(db_column='Destination', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'job_info_jobinfotable'


class LeaveProgressEmployeeemployeetable(models.Model):
    emp_id = models.CharField(db_column='Emp_id', primary_key=True, max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'leave_progress_employeeemployeetable'


class LeaveProgressLeaveprogresstable(models.Model):
    id = models.BigAutoField(primary_key=True)
    year = models.CharField(db_column='Year', max_length=10, blank=True, null=True)  # Field name made lowercase.
    leave_balance = models.IntegerField(db_column='Leave_balance', blank=True, null=True)  # Field name made lowercase.
    leaves_availed = models.IntegerField(db_column='Leaves_availed', blank=True, null=True)  # Field name made lowercase.
    emp_id = models.ForeignKey(LeaveProgressEmployeeemployeetable, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'leave_progress_leaveprogresstable'


class ManagementInfoManagementinfotable(models.Model):
    id = models.BigAutoField(primary_key=True)
    manager_emp_id = models.CharField(db_column='Manager_emp_id', max_length=10, blank=True, null=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    work_phone = models.CharField(db_column='Work_phone', max_length=10, blank=True, null=True)  # Field name made lowercase.
    manager_email = models.CharField(db_column='Manager_email', max_length=10, blank=True, null=True)  # Field name made lowercase.
    is_effective = models.IntegerField(blank=True, null=True)
    effective_start_date = models.DateField(db_column='Effective_start_date', blank=True, null=True)  # Field name made lowercase.
    effective_end_date = models.DateField(db_column='Effective_end_date', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_updated_by = models.CharField(db_column='Last_updated_by', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_updated_date = models.DateField(db_column='Last_updated_date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'management_info_managementinfotable'


class NationalInfoNationalinfotable(models.Model):
    id = models.BigAutoField(primary_key=True)
    national_id = models.CharField(db_column='National_id', max_length=10, blank=True, null=True)  # Field name made lowercase.
    card_type = models.CharField(db_column='Card_type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_updated_by = models.CharField(db_column='Last_updated_by', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_updated_date = models.DateField(db_column='Last_updated_date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'national_info_nationalinfotable'


class OrganizationOrganizationtable(models.Model):
    id = models.BigAutoField(primary_key=True)
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

    class Meta:
        managed = False
        db_table = 'organization_organizationtable'


class PersonalInfoPersonalinfotable(models.Model):
    first_name = models.CharField(db_column='First_name', primary_key=True, max_length=10)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    intial = models.CharField(db_column='Intial', max_length=5, blank=True, null=True)  # Field name made lowercase.
    marital_status = models.CharField(db_column='Marital_status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ethnicity_code = models.CharField(db_column='Ethnicity_code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    is_effective = models.IntegerField(blank=True, null=True)
    effective_start_date = models.DateField(db_column='Effective_start_date', blank=True, null=True)  # Field name made lowercase.
    effective_end_date = models.DateField(db_column='Effective_end_date', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_updated_by = models.CharField(db_column='Last_updated_by', max_length=10, blank=True, null=True)  # Field name made lowercase.
    last_updated_date = models.DateField(db_column='Last_updated_date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'personal_info_personalinfotable'


class QualificationQualificationtable(models.Model):
    id = models.BigAutoField(primary_key=True)
    class_field = models.CharField(db_column='Class', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    mark_percentage = models.IntegerField(db_column='Mark_percentage', blank=True, null=True)  # Field name made lowercase.
    pass_out_year = models.CharField(db_column='Pass_out_year', max_length=10, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=10, blank=True, null=True)  # Field name made lowercase.
    institution_name = models.CharField(db_column='Institution_name', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'qualification_qualificationtable'


class SkillsSkillstable(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_primary = models.IntegerField(blank=True, null=True)
    technology = models.CharField(db_column='Technology', max_length=10, blank=True, null=True)  # Field name made lowercase.
    years_of_experience = models.IntegerField(db_column='Years_of_experience', blank=True, null=True)  # Field name made lowercase.
    last_used = models.CharField(db_column='Last_used', max_length=10, blank=True, null=True)  # Field name made lowercase.
    certified = models.IntegerField(db_column='Certified', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'skills_skillstable'


class TimeSheetTimesheetinfotable(models.Model):
    id = models.BigAutoField(primary_key=True)
    week_start_date = models.DateField(db_column='Week_start_date', blank=True, null=True)  # Field name made lowercase.
    monday = models.CharField(db_column='Monday', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sunday = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'time_sheet_timesheetinfotable'
