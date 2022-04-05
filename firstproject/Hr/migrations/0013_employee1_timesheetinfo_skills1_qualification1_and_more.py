# Generated by Django 4.0.1 on 2022-04-04 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hr', '0012_delete_personalinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee1',
            fields=[
                ('id', models.IntegerField(db_column='Id')),
                ('empid', models.CharField(db_column='EmpId', max_length=10, primary_key=True, serialize=False)),
                ('effectivestartdate', models.DateField(blank=True, db_column='EffectiveStartDate', null=True)),
                ('effectiveenddate', models.DateField(blank=True, db_column='EffectiveEndDate', null=True)),
                ('lastupdatedby', models.CharField(blank=True, db_column='LastUpdatedBy', max_length=10, null=True)),
                ('lastupdateddate', models.DateField(blank=True, db_column='LastUpdatedDate', null=True)),
                ('hiredate', models.DateField(blank=True, db_column='HireDate', null=True)),
                ('oktorehire', models.CharField(blank=True, db_column='OkToRehire', max_length=10, null=True)),
                ('terminationdate', models.DateField(blank=True, db_column='TerminationDate', null=True)),
                ('benefitsstartdate', models.DateField(blank=True, db_column='BenefitsStartDate', null=True)),
                ('benefitsenddate', models.DateField(blank=True, db_column='BenefitsEndDate', null=True)),
                ('iseffective', models.IntegerField(blank=True, db_column='IsEffective', null=True)),
                ('totalyearsofexperience', models.CharField(blank=True, db_column='TotalYearsOfExperience', max_length=10, null=True)),
                ('action', models.CharField(blank=True, db_column='Action', max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Timesheetinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekstartdate', models.DateField(blank=True, db_column='WeekStartDate', null=True)),
                ('monday', models.CharField(blank=True, db_column='Monday', max_length=10, null=True)),
                ('sunday', models.CharField(blank=True, db_column='Sunday', max_length=10, null=True)),
                ('empid', models.ForeignKey(blank=True, db_column='EmpId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Hr.employee1')),
            ],
        ),
        migrations.CreateModel(
            name='Skills1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isprimary', models.IntegerField(blank=True, db_column='IsPrimary', null=True)),
                ('technology', models.CharField(blank=True, db_column='Technology', max_length=10, null=True)),
                ('yearsofexperience', models.IntegerField(blank=True, db_column='YearsOfExperience', null=True)),
                ('lastused', models.CharField(blank=True, db_column='LastUsed', max_length=10, null=True)),
                ('certified', models.IntegerField(blank=True, db_column='Certified', null=True)),
                ('empid', models.ForeignKey(blank=True, db_column='EmpId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Hr.employee1')),
            ],
        ),
        migrations.CreateModel(
            name='Qualification1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_field', models.CharField(blank=True, db_column='Class', max_length=10, null=True)),
                ('markpercentage', models.IntegerField(blank=True, db_column='MarkPercentage', null=True)),
                ('passoutyear', models.CharField(blank=True, db_column='PassOutYear', max_length=10, null=True)),
                ('location', models.CharField(blank=True, db_column='Location', max_length=10, null=True)),
                ('institutionname', models.CharField(blank=True, db_column='InstitutionName', max_length=10, null=True)),
                ('empid', models.ForeignKey(blank=True, db_column='EmpId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Hr.employee1')),
            ],
        ),
        migrations.CreateModel(
            name='Personalinfo',
            fields=[
                ('firstname', models.CharField(db_column='FirstName', max_length=10, primary_key=True, serialize=False)),
                ('lastname', models.CharField(blank=True, db_column='LastName', max_length=10, null=True)),
                ('gender', models.CharField(blank=True, db_column='Gender', max_length=10, null=True)),
                ('dob', models.DateField(blank=True, db_column='DOB', null=True)),
                ('intial', models.CharField(blank=True, db_column='Intial', max_length=5, null=True)),
                ('maritalstatus', models.CharField(blank=True, db_column='MaritalStatus', max_length=10, null=True)),
                ('ethnicitycode', models.CharField(blank=True, db_column='EthnicityCode', max_length=10, null=True)),
                ('iseffective', models.IntegerField(blank=True, db_column='IsEffective', null=True)),
                ('effectivestartdate', models.DateField(blank=True, db_column='EffectiveStartDate', null=True)),
                ('effectiveenddate', models.DateField(blank=True, db_column='EffectiveEndDate', null=True)),
                ('action', models.CharField(blank=True, db_column='Action', max_length=10, null=True)),
                ('lastupdatedby', models.CharField(blank=True, db_column='LastUpdatedBy', max_length=10, null=True)),
                ('lastupdateddate', models.DateField(blank=True, db_column='LastUpdatedDate', null=True)),
                ('empid', models.ForeignKey(blank=True, db_column='EmpId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Hr.employee1')),
            ],
        ),
        migrations.CreateModel(
            name='Organization1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizationtype', models.CharField(blank=True, db_column='OrganizationType', max_length=10, null=True)),
                ('country', models.CharField(blank=True, db_column='Country', max_length=10, null=True)),
                ('company', models.CharField(blank=True, db_column='Company', max_length=10, null=True)),
                ('companycode', models.CharField(blank=True, db_column='CompanyCode', max_length=10, null=True)),
                ('companyname', models.CharField(blank=True, db_column='CompanyName', max_length=10, null=True)),
                ('accountcode', models.CharField(blank=True, db_column='AccountCode', max_length=10, null=True)),
                ('accountbtname', models.CharField(blank=True, db_column='AccountBtName', max_length=10, null=True)),
                ('address1', models.CharField(blank=True, db_column='Address1', max_length=20, null=True)),
                ('address2', models.CharField(blank=True, db_column='Address2', max_length=20, null=True)),
                ('address3', models.CharField(blank=True, db_column='Address3', max_length=20, null=True)),
                ('city', models.CharField(blank=True, db_column='City', max_length=10, null=True)),
                ('postalcode', models.CharField(blank=True, db_column='PostalCode', max_length=10, null=True)),
                ('state', models.CharField(blank=True, db_column='State', max_length=10, null=True)),
                ('empid', models.ForeignKey(blank=True, db_column='EmpId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Hr.employee1')),
            ],
        ),
        migrations.CreateModel(
            name='Nationalinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nationalid', models.CharField(blank=True, db_column='NationalId', max_length=10, null=True)),
                ('cardtype', models.CharField(blank=True, db_column='CardType', max_length=10, null=True)),
                ('action', models.CharField(blank=True, db_column='Action', max_length=10, null=True)),
                ('lastupdatedby', models.CharField(blank=True, db_column='LastUpdatedBy', max_length=10, null=True)),
                ('lastupdateddate', models.DateField(blank=True, db_column='LastUpdatedDate', null=True)),
                ('empid', models.ForeignKey(blank=True, db_column='EmpId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Hr.employee1')),
            ],
        ),
        migrations.CreateModel(
            name='Managementinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('managerempid', models.CharField(blank=True, db_column='ManagerEmpId', max_length=10, null=True)),
                ('firstname', models.CharField(blank=True, db_column='FirstName', max_length=10, null=True)),
                ('lastname', models.CharField(blank=True, db_column='LastName', max_length=10, null=True)),
                ('workphone', models.CharField(blank=True, db_column='WorkPhone', max_length=10, null=True)),
                ('manageremail', models.CharField(blank=True, db_column='ManagerEmail', max_length=10, null=True)),
                ('iseffective', models.IntegerField(blank=True, db_column='IsEffective', null=True)),
                ('effectivestartdate', models.DateField(blank=True, db_column='EffectiveStartDate', null=True)),
                ('effectiveenddate', models.DateField(blank=True, db_column='EffectiveEndDate', null=True)),
                ('action', models.CharField(blank=True, db_column='Action', max_length=10, null=True)),
                ('lastupdatedby', models.CharField(blank=True, db_column='LastUpdatedBy', max_length=10, null=True)),
                ('lastupdateddate', models.DateField(blank=True, db_column='LastUpdatedDate', null=True)),
                ('empid', models.ForeignKey(blank=True, db_column='EmpId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Hr.employee1')),
            ],
        ),
        migrations.CreateModel(
            name='Leaveinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(blank=True, db_column='Year', max_length=10, null=True)),
                ('leavebalance', models.IntegerField(blank=True, db_column='LeaveBalance', null=True)),
                ('leavesavailed', models.IntegerField(blank=True, db_column='LeavesAvailed', null=True)),
                ('empid', models.ForeignKey(blank=True, db_column='EmpId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Hr.employee1')),
            ],
        ),
        migrations.CreateModel(
            name='Jobinfo',
            fields=[
                ('personid', models.CharField(db_column='PersonId', max_length=10, primary_key=True, serialize=False)),
                ('jobname', models.CharField(blank=True, db_column='JobName', max_length=10, null=True)),
                ('employeecclass', models.CharField(blank=True, db_column='EmployeecClass', max_length=10, null=True)),
                ('employeetype', models.CharField(blank=True, db_column='EmployeeType', max_length=10, null=True)),
                ('employeestatus', models.CharField(blank=True, db_column='EmployeeStatus', max_length=10, null=True)),
                ('jobstartdate', models.DateField(blank=True, db_column='JobStartDate', null=True)),
                ('positionstartdate', models.DateField(blank=True, db_column='PositionStartDate', null=True)),
                ('isfulltimeemployee', models.IntegerField(blank=True, db_column='IsFulltimeEmployee', null=True)),
                ('jobtitle', models.CharField(blank=True, db_column='JobTitle', max_length=10, null=True)),
                ('position', models.CharField(blank=True, db_column='Position', max_length=10, null=True)),
                ('positionname', models.CharField(blank=True, db_column='PositionName', max_length=10, null=True)),
                ('standardhours', models.CharField(blank=True, db_column='StandardHours', max_length=10, null=True)),
                ('costcenter', models.CharField(blank=True, db_column='CostCenter', max_length=10, null=True)),
                ('costcentername', models.CharField(blank=True, db_column='CostCenterName', max_length=10, null=True)),
                ('clientbasedhiredate', models.DateField(blank=True, db_column='ClientBasedHireDate', null=True)),
                ('destination', models.CharField(blank=True, db_column='Destination', max_length=10, null=True)),
                ('empid', models.ForeignKey(blank=True, db_column='EmpId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Hr.employee1')),
            ],
        ),
        migrations.CreateModel(
            name='Experience1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previousorgname', models.CharField(blank=True, db_column='PreviousOrgName', max_length=10, null=True)),
                ('startperiod', models.CharField(blank=True, db_column='StartPeriod', max_length=10, null=True)),
                ('endperiod', models.CharField(blank=True, db_column='EndPeriod', max_length=10, null=True)),
                ('yearsofexperience', models.IntegerField(blank=True, db_column='yearsOfExperience', null=True)),
                ('referencename', models.CharField(blank=True, db_column='ReferenceName', max_length=10, null=True)),
                ('referencecontact', models.CharField(blank=True, db_column='ReferenceContact', max_length=10, null=True)),
                ('empid', models.ForeignKey(blank=True, db_column='EmpId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Hr.employee1')),
            ],
        ),
        migrations.CreateModel(
            name='Emergencycontact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primaryflag', models.CharField(blank=True, db_column='PrimaryFlag', max_length=10, null=True)),
                ('relationship', models.CharField(blank=True, db_column='Relationship', max_length=10, null=True)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=10, null=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('action', models.CharField(blank=True, db_column='Action', max_length=10, null=True)),
                ('lastupdatedby', models.CharField(blank=True, db_column='LastUpdatedBy', max_length=10, null=True)),
                ('lastupdateddate', models.DateField(blank=True, db_column='LastUpdatedDate', null=True)),
                ('empid', models.ForeignKey(blank=True, db_column='EmpId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Hr.employee1')),
            ],
        ),
        migrations.CreateModel(
            name='Contact1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneno', models.CharField(blank=True, db_column='PhoneNo', max_length=10, null=True)),
                ('phonetype', models.CharField(blank=True, db_column='PhoneType', max_length=10, null=True)),
                ('countrycode', models.CharField(blank=True, db_column='CountryCode', max_length=10, null=True)),
                ('extension', models.CharField(blank=True, db_column='Extension', max_length=10, null=True)),
                ('action', models.CharField(blank=True, db_column='Action', max_length=10, null=True)),
                ('lastupdatedby', models.CharField(blank=True, db_column='LastUpdatedBy', max_length=10, null=True)),
                ('lastupdateddate', models.DateField(blank=True, db_column='LastUpdatedDate', null=True)),
                ('addresstype', models.CharField(blank=True, db_column='AddressType', max_length=10, null=True)),
                ('address1', models.CharField(blank=True, db_column='Address1', max_length=20, null=True)),
                ('city', models.CharField(blank=True, db_column='City', max_length=10, null=True)),
                ('postalcode', models.CharField(blank=True, db_column='PostalCode', max_length=10, null=True)),
                ('state', models.CharField(blank=True, db_column='State', max_length=10, null=True)),
                ('country', models.CharField(blank=True, db_column='Country', max_length=10, null=True)),
                ('iseffective', models.IntegerField(blank=True, db_column='IsEffective', null=True)),
                ('effectivestartdate', models.DateField(blank=True, db_column='EffectiveStartDate', null=True)),
                ('effectiveenddate', models.DateField(blank=True, db_column='EffectiveEndDate', null=True)),
                ('empid', models.ForeignKey(blank=True, db_column='EmpId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Hr.employee1')),
            ],
        ),
        migrations.CreateModel(
            name='Bankdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankname', models.CharField(blank=True, db_column='BankName', max_length=10, null=True)),
                ('branch', models.CharField(blank=True, db_column='Branch', max_length=10, null=True)),
                ('accountnumber', models.CharField(blank=True, db_column='AccountNumber', max_length=10, null=True)),
                ('ifsccode', models.CharField(blank=True, db_column='IFSCCode', max_length=10, null=True)),
                ('beneficiaryname', models.CharField(blank=True, db_column='BeneficiaryName', max_length=10, null=True)),
                ('accounttype', models.CharField(blank=True, db_column='AccountType', max_length=10, null=True)),
                ('routingnumber', models.CharField(blank=True, db_column='RoutingNumber', max_length=10, null=True)),
                ('empid', models.ForeignKey(blank=True, db_column='EmpId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Hr.employee1')),
            ],
        ),
        migrations.AlterField(
            model_name='compensationinfo',
            name='empid',
            field=models.ForeignKey(blank=True, db_column='EmpId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Hr.employee1'),
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
