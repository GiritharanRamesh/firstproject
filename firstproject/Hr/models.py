from django.db import models


class Employee1(models.Model):
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



class Compensationinfo(models.Model):
    empid = models.ForeignKey('Employee1', models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.
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



class Contact1(models.Model):
    empid = models.ForeignKey('Employee1', models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.
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



class Emergencycontact(models.Model):
    empid = models.ForeignKey('Employee1', models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.
    primaryflag = models.CharField(db_column='PrimaryFlag', max_length=10, blank=True, null=True)  # Field name made lowercase.
    relationship = models.CharField(db_column='Relationship', max_length=10, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=10, blank=True, null=True)
    action = models.CharField(db_column='Action', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.CharField(db_column='LastUpdatedBy', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.



class Experience1(models.Model):
    empid = models.ForeignKey('Employee1', models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.
    previousorgname = models.CharField(db_column='PreviousOrgName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    startperiod = models.CharField(db_column='StartPeriod', max_length=10, blank=True, null=True)  # Field name made lowercase.
    endperiod = models.CharField(db_column='EndPeriod', max_length=10, blank=True, null=True)  # Field name made lowercase.
    yearsofexperience = models.IntegerField(db_column='yearsOfExperience', blank=True, null=True)  # Field name made lowercase.
    referencename = models.CharField(db_column='ReferenceName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    referencecontact = models.CharField(db_column='ReferenceContact', max_length=10, blank=True, null=True)  # Field name made lowercase



class Jobinfo(models.Model):
    empid = models.ForeignKey('Employee1', models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.
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



class Leaveinfo(models.Model):
    empid = models.ForeignKey('Employee1', models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=10, blank=True, null=True)  # Field name made lowercase.
    leavebalance = models.IntegerField(db_column='LeaveBalance', blank=True, null=True)  # Field name made lowercase.
    leavesavailed = models.IntegerField(db_column='LeavesAvailed', blank=True, null=True)  # Field name made lowercase.



class Managementinfo(models.Model):
    empid = models.ForeignKey('Employee1', models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.
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



class Nationalinfo(models.Model):
    empid = models.ForeignKey('Employee1', models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.
    nationalid = models.CharField(db_column='NationalId', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cardtype = models.CharField(db_column='CardType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.CharField(db_column='LastUpdatedBy', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.



class Organization1(models.Model):
    empid = models.ForeignKey('Employee1', models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.
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



class Personalinfo(models.Model):
    empid = models.ForeignKey('Employee1', models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.
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



class Qualification1(models.Model):
    empid = models.ForeignKey('Employee1', models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    markpercentage = models.IntegerField(db_column='MarkPercentage', blank=True, null=True)  # Field name made lowercase.
    passoutyear = models.CharField(db_column='PassOutYear', max_length=10, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=10, blank=True, null=True)  # Field name made lowercase.
    institutionname = models.CharField(db_column='InstitutionName', max_length=10, blank=True, null=True)  # Field name made lowercase.



class Skills1(models.Model):
    empid = models.ForeignKey('Employee1', models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.
    isprimary = models.IntegerField(db_column='IsPrimary', blank=True, null=True)  # Field name made lowercase.
    technology = models.CharField(db_column='Technology', max_length=10, blank=True, null=True)  # Field name made lowercase.
    yearsofexperience = models.IntegerField(db_column='YearsOfExperience', blank=True, null=True)  # Field name made lowercase.
    lastused = models.CharField(db_column='LastUsed', max_length=10, blank=True, null=True)  # Field name made lowercase.
    certified = models.IntegerField(db_column='Certified', blank=True, null=True)  # Field name made lowercase.


class Timesheetinfo(models.Model):
    empid = models.ForeignKey('Employee1', models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.
    weekstartdate = models.DateField(db_column='WeekStartDate', blank=True, null=True)  # Field name made lowercase.
    monday = models.CharField(db_column='Monday', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sunday = models.CharField(db_column='Sunday', max_length=10, blank=True, null=True)



class Bankdetails(models.Model):
    empid = models.ForeignKey('Employee1', models.DO_NOTHING, db_column='EmpId', blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=10, blank=True, null=True)  # Field name made lowercase.
    accountnumber = models.CharField(db_column='AccountNumber', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ifsccode = models.CharField(db_column='IFSCCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    beneficiaryname = models.CharField(db_column='BeneficiaryName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    accounttype = models.CharField(db_column='AccountType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    routingnumber = models.CharField(db_column='RoutingNumber', max_length=10, blank=True, null=True)  # Field name made lowercase










