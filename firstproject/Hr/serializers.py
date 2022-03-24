from .models import Employee1, Compensationinfo, Contact1, Emergencycontact, Experience1, Jobinfo, Leaveinfo, Managementinfo, Nationalinfo, Organization1, Personalinfo, Qualification1, Skills1, Timesheetinfo, Bankdetails
from rest_framework import serializers
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee1
        fields = ('empid', 'effectivestartdate', 'effectiveenddate', 'lastupdatedby', 'lastupdateddate', 'hiredate', 'oktorehire', 'terminationdate', 'benefitsstartdate', 'benefitsenddate', 'iseffective', 'totalyearsofexperience', 'action')

class CompensationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compensationinfo
        fields = ('empid', 'currency', 'basic', 'dearnessallowance', 'hra', 'conveyanceallowance', 'specialallowance', 'salaryadvance', 'pfemployee', 'esicemployee', 'pt', 'pfemployercont', 'esicemployercont', 'iseffective', 'effectivestartdate', 'effectiveenddate', 'action', 'lastupdatedby', 'lastupdateddate')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact1
        fields = ('empid', 'phoneno', 'phonetype', 'countrycode', 'extension', 'action', 'lastupdatedby', 'lastupdateddate', 'addresstype', 'address1', 'city', 'postalcode', 'state', 'country', 'iseffective', 'effectivestartdate', 'effectiveenddate')


class EmergencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Emergencycontact
        fields = ('empid', 'primaryflag', 'relationship', 'name', 'phone', 'action', 'lastupdatedby', 'lastupdateddate')


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience1
        fields = ('empid', 'previousorgname', 'startperiod', 'endperiod', 'yearsofexperience', 'referencename', 'referencecontact')


class JobInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobinfo
        fields = ('empid', 'personid', 'jobname', 'employeeclass', 'employeetype', 'employeestatus', 'jobstartdate', 'positionstartdate', 'isfulltimeemployee', 'jobtitle', 'position', 'positionname', 'standardhours', 'costcenter', 'costcentername', 'clientbasedhiredate', 'destination')


class LeaveInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaveinfo
        fields = ('empid', 'year', 'leavebalance', 'leavesavailed')


class ManagementInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Managementinfo
        fields = ('empid', 'managerempid', 'firstname', 'lastname', 'workphone', 'manageremail', 'iseffective', 'effectivestartdate', 'effectiveenddate', 'action', 'lastupdatedby', 'lastupdateddate')


class NationalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nationalinfo
        fields = ('empid', 'nationalid', 'cardtype', 'action', 'lastupdatedby', 'lastupdateddate')


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization1
        fields = ('empid', 'organizationtype', 'country', 'company', 'companycode', 'companyname', 'accountcode', 'accountbtname', 'address1', 'address2', 'address3', 'city', 'postalcode', 'state')


class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personalinfo
        fields = ('empid', 'firstname', 'lastname', 'gender', 'dob', 'intial', 'maritalstatus', 'ethnicitycode', 'iseffective', 'effectivestartdate', 'effectiveenddate', 'action', 'lastupdatedby', 'lastupdateddate')


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification1
        fields = ('empid', 'classfield', 'markpercentage', 'passoutyear', 'location', 'institutionname')


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills1
        fields = ('empid', 'isprimary', 'technology', 'yearsofexperience', 'lastused', 'certified')


class TimeSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timesheetinfo
        fields = ('empid', 'weekstartdate', 'monday', 'sunday')



class BankDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bankdetails
        fields = ('empid', 'bankname', 'branch', 'accountno', 'ifsccode', 'beneficiaryname', 'accounttype', 'routingnumber')