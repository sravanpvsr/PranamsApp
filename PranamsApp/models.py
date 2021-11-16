from django.db import models
from django.utils.html import mark_safe
from calendar import monthrange
import calendar
from datetime import datetime
from datetime import date
from datetime import timedelta
from river.models.fields.state import StateField

## Blood Group Dropdown
BLOOD_GROUP_CHOICES = (
    ('A+','A+'),
    ('A-', 'A-'),
    ('O+','O+'),
    ('O-','O-'),
    ('B+','B+'),
    ('B-','B-'),
    ('AB+','AB+'),
    ('AB-','AB-'),
)

TWO_FOUR_WHEELER = (
    ('two','Two'),
    ('four', 'Four'),
)

RELATIONSHIP_CHOICES = (
    ('father','Father'),
    ('mother','Mother'),
    ('spouse','Spouse'),
    ('son','Son'),
    ('daughter','Daughter'),
    ('brother','Brother'),
    ('sister','Sister'),
    ('grandSon','Grand Son'),
    ('grandDaughter','Grand Daughter'),
    ('niece','Niece'),
    ('nephew','Nephew'),
    ('colleague','Colleague'),
    ('others','Others')    
)

RELATION_CHOICES =(
    ('wo','W/O'),
    ('do','D/O'),
    ('so','S/O'),
)


# Create your models here.
class Member_Category_Master(models.Model):
    Member_Category_ID=models.CharField(primary_key=True,max_length=10)
    Member_Category=models.CharField(max_length=50)
    Updated_Date=models.DateField()
    Updated_By=models.CharField(max_length=20)
    Status=models.CharField(max_length=1)
    def __str__(self):
        return self.Member_Category

    

class Institution_Master(models.Model):
    Institution_ID=models.CharField(primary_key=True,max_length=20)
    Institution_Name=models.CharField(max_length=100)
    Updated_Date=models.DateField()
    Updated_By=models.CharField(max_length=20)
    Status=models.CharField(max_length=1)
    def __str__(self):
        return self.Institution_Name
    

class Sub_Division_Master(models.Model):
    Sub_Division_ID=models.CharField(primary_key=True,max_length=20)
    Sub_Division_Name=models.CharField(max_length=100)
    Updated_Date=models.DateField()
    Updated_By=models.CharField(max_length=20)
    Status=models.CharField(max_length=1)
    def __str__(self):
        return self.Sub_Division_Name
    

class Institution_Sub_Division_Map(models.Model):
    Institution_ID=models.ForeignKey(Institution_Master, on_delete=models.CASCADE)
    Sub_Division_ID=models.ForeignKey(Sub_Division_Master, on_delete=models.CASCADE)
    Updated_Date=models.DateField()
    Updated_By=models.CharField(max_length=20)
    Status=models.CharField(max_length=1)
    

class Room_Type_Master(models.Model):
    Room_Type_ID=models.CharField(primary_key=True,max_length=10)
    Room_Type_Desc=models.CharField(max_length=20)
    Updated_Date=models.DateField()
    Updated_By=models.CharField(max_length=20)
    Status=models.CharField(max_length=1)
    def __str__(self):
        return self.Room_Type_Desc

class Room_Master(models.Model):
    Room=models.CharField(primary_key=True,max_length=10)
    Room_Type_ID=models.ForeignKey(Room_Type_Master, on_delete=models.CASCADE)
    Updated_Date=models.DateField()
    Updated_By=models.CharField(max_length=20)
    Status=models.CharField(max_length=1)
    def __str__(self):
        return self.Room

# class Member_Master(models.Model):
#     Member_PRANAMS_ID=models.IntegerField(primary_key=True)
#     Member_Name=models.CharField(max_length=100,blank=True, null=True)   
#     Updated_Date=models.DateField(blank=True, null=True)
#     Updated_By=models.CharField(max_length=20,blank=True, null=True)
#     Status=models.CharField(max_length=1,blank=True, null=True)
#     Occupant_Member=models.CharField(max_length=15, blank=True, null=True)

# class Member_Accommodation(models.Model):
#     Member_PRANAMS_ID=models.ForeignKey(Member_Master, on_delete=models.CASCADE)
#     Room=models.ForeignKey(Room_Master, on_delete=models.CASCADE)
#     Updated_Date=models.DateField()
#     Updated_By=models.CharField(max_length=20)
#     Status=models.CharField(max_length=1)


# class Occupant_Master(models.Model):
#     #Member_PRANAMS_ID=models.ForeignKey(Member_Master, on_delete=models.CASCADE)
#     Occ_Name=models.CharField(max_length=100)
#     Occ_DOB=models.DateField()
#     Occ_Relationship=models.CharField(max_length=20)
#     Occ_Permanent_Resident_Not=models.CharField(max_length=1)
#     Occ_Aadhaar_ID=models.IntegerField()
#     #Occupant_PRANAMS_ID=models.CharField(primary_key=True,max_length=10)
#     #Occ_DL_No=models.CharField(max_length=50)
#     Status=models.CharField(max_length=1)
#     Updated_Date=models.DateField()
#     Updated_By=models.CharField(max_length=20)
#     Status=models.CharField(max_length=1)
CHOICES = (
    ('yes','Yes'),
    ('no','No')
)
MEMBER_CHOICES=(
    ('member','Primary Member'),
    ('occupant','Occupant')
)

VEHICLE_OWNER_CHOICES=(
    ('ashramResident','Ashram Resident'),
    ('notAshramResident','Residing Outside Ashram')
)

VEHICLE_TYPE_CHOICES=(
    ('taxi','Taxi'),
    ('tatamagic','Tata Magic'),
    ('van','Van'),
    ('bus','Bus'),
    ('car','Car')
)
# class Vehicle_Master(models.Model):
#     Room=models.ForeignKey(Room_Master, on_delete=models.CASCADE)
#     Vehicle_Available=models.CharField(max_length=3, choices=CHOICES)
#     Member_Occupant=models.CharField(max_length=15, choices=MEMBER_CHOICES)
#     Member_Name=models.ForeignKey(Member_Master, on_delete=models.CASCADE)
#     #Vehicle_PRANAMS_ID=models.CharField(primary_key=True,max_length=10)
#     Vehicle_No=models.CharField(max_length=20)
#     Two_Four_Wheeler=models.CharField(max_length=1)
#     RC_No=models.CharField(max_length=30)
#     RC_Valid_Upto=models.DateField()
#     Occupant_PRANAMS_ID=models.CharField(max_length=30)
#     Insurance_Valid_Upto=models.DateField()
#     Entry_Extended_By=models.CharField(max_length=30)
#     Remarks=models.CharField(max_length=200)
#     Updated_Date=models.DateField()
#     Updated_By=models.CharField(max_length=20)
#     Status=models.CharField(max_length=1)
     

class Gate_Master(models.Model):
    Gate_ID=models.CharField(primary_key=True,max_length=5)
    Gate_Name=models.CharField(max_length=50)
    Updated_Date=models.DateField()
    Updated_By=models.CharField(max_length=20)
    Status=models.CharField(max_length=1)
    def __str__(self):
        return self.Gate_Name

# class Occupant_Master(models.Model):
#     Occ_ID=models.IntegerField(primary_key=True)
#     Room=models.ForeignKey(Room_Master, on_delete=models.CASCADE)
#     Staff_Choice = models.CharField(max_length=5, choices=CHOICES)     
#     #Room_Type=models.ForeignKey(Room_Type_Master, on_delete=models.CASCADE, blank=True)
#     Name=models.CharField(max_length=100)
#     DOB=models.DateField()
#     Aadhaar_ID=models.IntegerField()
#     Relationship_With_Primary_Member=models.CharField(max_length=20, choices=RELATIONSHIP_CHOICES)
#     Permanent_Resident_Or_Not=models.CharField(blank=True,max_length=5, choices=CHOICES)
#     Blood_Group=models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES,blank=True)
#     Occupant_Category=models.ForeignKey(Member_Category_Master, on_delete=models.CASCADE,blank=True)
#     Institution_Name=models.ForeignKey(Institution_Master, on_delete=models.CASCADE, blank=True)
#     Sub_Division_Name=models.ForeignKey(Sub_Division_Master, on_delete=models.CASCADE, blank=True)
#     Staff_Working_Since=models.DateField(blank=True)
#     Staff_Designation=models.CharField(max_length=50, blank=True)
#     Staff_Institution_Emp_ID=models.CharField(max_length=20, blank=True)
#     Mobile=models.IntegerField(blank=True)
#     Whatsapp_Choice = models.CharField(max_length=5, choices=CHOICES, blank=True)
#     Whatsapp=models.IntegerField(blank=True)
#     Photo_File_Name=models.CharField(max_length=150,blank=True)  
#     #Staff_Choice = models.CharField(max_length=5, choices=CHOICES)     
#     #Member_DL_No=models.CharField(max_length=50)
#     #Member_DL_Validity=models.DateField()    
#     #Address_Outside_PSN=models.CharField(max_length=200, blank=True)
#     Emergency_Contact_Name=models.CharField(max_length=40,blank=True)
#     Emergency_Contact_Email=models.CharField(max_length=40,blank=True)
#     Emergency_Contact_Relationship=models.CharField(max_length=20, choices=RELATIONSHIP_CHOICES,blank=True)
#     Emergency_Contact_ISD=models.CharField(max_length=20,blank=True)
#     Emergency_Contact_Mobile_No=models.IntegerField(blank=True)
#     Emergency_Contact_Address=models.CharField(max_length=200,blank=True)
#     Updated_Date=models.DateTimeField(auto_now_add = True)
#     Updated_By=models.CharField(max_length=10,default='Admin')
#     Status=models.CharField(max_length=2,default='Y')

# class add_demography(models.Model):
#     Member_Category=models.ForeignKey(Member_Category_Master, on_delete=models.CASCADE)
#     Room=models.ForeignKey(Room_Master, on_delete=models.CASCADE, blank=True)
#     Room_Type=models.ForeignKey(Room_Type_Master, on_delete=models.CASCADE, blank=True)
#     Member_Name=models.CharField(max_length=100)
#     Member_DOB=models.DateField()
#     Member_Blood_Group=models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
#     Institution_Name=models.ForeignKey(Institution_Master, on_delete=models.CASCADE, blank=True)
#     Sub_Division_Name=models.ForeignKey(Sub_Division_Master, on_delete=models.CASCADE, blank=True)
#     Staff_Working_Since=models.DateField(blank=True)
#     Staff_Designation=models.CharField(max_length=50, blank=True)
#     Staff_Institution_Emp_ID=models.CharField(max_length=20, blank=True)
#     Member_Mobile=models.IntegerField()
#     Whatsapp_Choice = models.CharField(max_length=5, choices=CHOICES)
#     Member_Whatsapp=models.IntegerField(blank=True)    
#     #Staff_Choice = models.CharField(max_length=5, choices=CHOICES)     
#     Member_Aadhaar_ID=models.IntegerField()
#     #Member_DL_No=models.CharField(max_length=50)
#     #Member_DL_Validity=models.DateField()    
#     Address_Outside_PSN=models.CharField(max_length=200, blank=True)
#     Emergency_Contact_Name=models.CharField(max_length=40)
#     Emergency_Contact_Email=models.CharField(max_length=40)
#     Emergency_Contact_Relationship=models.CharField(max_length=20, choices=RELATIONSHIP_CHOICES)
#     Emergency_Contact_ISD=models.CharField(max_length=20)
#     Emergency_Contact_Mobile_No=models.IntegerField()
#     Emergency_Contact_Address=models.CharField(max_length=200)
#     Member_Photo_File_Name=models.ImageField(upload_to="media") 
#     Updated_Date=models.DateTimeField(auto_now_add = True)
#     Updated_By=models.CharField(max_length=10,default='Admin')
#     Status=models.CharField(max_length=2,default='Y')

class Demography(models.Model):
    Room=models.ForeignKey(Room_Master, on_delete=models.CASCADE, blank=True,null=True)
    Member_Occupant= models.CharField(max_length=15, choices=MEMBER_CHOICES,
    verbose_name="Is the Occupant a Staff/ Not?",null=True,blank=True)
    Category=models.ForeignKey(Member_Category_Master, on_delete=models.CASCADE,blank=True,null=True)
    Relationship_With_Primary_Member=models.CharField(max_length=20, choices=RELATIONSHIP_CHOICES,null=True,blank=True)
    #Permanent_Resident_Or_Not=models.CharField(blank=True,max_length=5, choices=CHOICES,null=True)
    Room_Type=models.ForeignKey(Room_Type_Master, on_delete=models.CASCADE, blank=True,null=True)
    Name=models.CharField(max_length=100)
    DOB=models.DateField(blank=True,null=True,verbose_name="Date of Birth in YYYY-MM-DD")
    Aadhaar_ID=models.IntegerField(blank=True,null=True)
    Mobile=models.IntegerField(blank=True,null=True)
    Whatsapp_Choice = models.CharField(max_length=5, choices=CHOICES,blank=True,null=True)
    Whatsapp=models.IntegerField(blank=True,null=True)
    Landline_Number=models.IntegerField(blank=True,null=True)
    Email=models.CharField(max_length=100,blank=True,null=True)
    Blood_Group=models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES,blank=True,null=True)
    SSSIHMS_PG_Patient_ID=models.CharField(max_length=20,blank=True,null=True)
    Institution_Name=models.ForeignKey(Institution_Master, on_delete=models.CASCADE, blank=True,null=True)
    Sub_Division_Name=models.ForeignKey(Sub_Division_Master, on_delete=models.CASCADE, blank=True,null=True)
    Staff_Working_Since=models.DateField(blank=True, null=True,verbose_name="Staff Working Since in YYYY-MM-DD")
    #Staff_Designation=models.CharField(max_length=50, blank=True,null=True)
    Staff_Institution_Emp_ID=models.CharField(max_length=20, blank=True,null=True)    
    #Staff_Choice = models.CharField(max_length=5, choices=CHOICES)     
    #Member_DL_No=models.CharField(max_length=50)
    #Member_DL_Validity=models.DateField()    
    #Address_Outside_PSN=models.CharField(max_length=200, blank=True,null=True)
    # Emergency_Contact_Name=models.CharField(max_length=40, blank=True,null=True)
    # Emergency_Contact_Email=models.CharField(max_length=40, blank=True,null=True)
    # Emergency_Contact_Relationship=models.CharField(max_length=20, choices=RELATIONSHIP_CHOICES, blank=True,null=True)
    # Emergency_Contact_ISD=models.CharField(max_length=20, blank=True,null=True)
    # Emergency_Contact_Mobile_No=models.IntegerField( blank=True,null=True)
    # Emergency_Contact_Address=models.CharField(max_length=200, blank=True,null=True)
    Photo_File_Name=models.ImageField(upload_to="", blank=True,null=True)
    Remarks=models.CharField(max_length=500,blank=True,null=True)
    Updated_Date=models.DateTimeField(auto_now_add = True)
    Updated_By=models.CharField(max_length=10,default='Admin')
    Status=models.CharField(max_length=2,default='Y')
    my_state_field = StateField()
    def __str__(self):
        return self.Name
    
    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.Photo_File_Name))

    image_tag.short_description = 'Image'

# class add_vehicle(models.Model):
#     Room=models.ForeignKey(Room_Master, on_delete=models.CASCADE)
#     Vehicle_Available=models.CharField(max_length=3, choices=CHOICES)
#     Member_Occupant=models.CharField(max_length=15,choices=MEMBER_CHOICES)
#     #Name=models.ForeignKey(add_demography,on_delete=models.CASCADE)
#     #Member_PRANAMS_ID=models.ForeignKey(Member_Master, on_delete=models.CASCADE)
#     #Occupant_Name=models.ForeignKey(Occupant_Master, on_delete=models.CASCADE)
#     #Vehicle_PRANAMS_ID=models.CharField(primary_key=True,max_length=10)
#     DL_No=models.CharField(max_length=50)
#     DL_Validity=models.DateField()
#     Two_Four_Wheeler=models.CharField(max_length=5,choices=TWO_FOUR_WHEELER)
#     Vehicle_No=models.CharField(max_length=20)
#     RC_No=models.CharField(max_length=30)
#     RC_Valid_Upto=models.DateField()
#     #Occupant_PRANAMS_ID=models.ForeignKey(Occupant_Master, on_delete=models.CASCADE)
#     Insurance_Valid_Upto=models.DateField()
#     #Entry_Extended_By=models.CharField(max_length=30)
#     Remarks=models.CharField(max_length=200)
#     Updated_Date=models.DateTimeField(auto_now_add = True)
#     Updated_By=models.CharField(max_length=20)
#     Status=models.CharField(max_length=1)
#     Gate_Name=models.ManyToManyField(Gate_Master)

#     def __str__(self):
#         return self.name

#Updated one -- 8-Jul-2021
class Vehicle(models.Model):
    Type_Of_Owner=models.CharField(max_length=50,choices=VEHICLE_OWNER_CHOICES)
    Room=models.ForeignKey(Room_Master, on_delete=models.CASCADE)
    #Vehicle_Available=models.CharField(max_length=3, choices=CHOICES)
    Member_Occupant=models.CharField(max_length=15,choices=MEMBER_CHOICES,)
    Member_Name=models.ForeignKey(Demography,on_delete=models.CASCADE,
                        null=True,blank=True)
    Owner_Name = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.IntegerField(blank=True,null=True) #TO enable 
    #Member_PRANAMS_ID=models.ForeignKey(Member_Master, on_delete=models.CASCADE)
    #Occupant_Name=models.ForeignKey(Occupant_Master, on_delete=models.CASCADE)
    #Vehicle_PRANAMS_ID=models.CharField(primary_key=True,max_length=10)
    Vehicle_No=models.CharField(max_length=20)
    Two_Four_Wheeler=models.CharField(max_length=5,choices=TWO_FOUR_WHEELER)
    #Validity=models.DateField(null=True,blank=True,verbose_name="Vehicle Allowed till in YYYY-MM-DD") 
    DL_No=models.CharField(max_length=50,null=True,blank=True)
    DL_Validity=models.DateField(verbose_name="DL Valid Upto in YYYY-MM-DD",null=True,blank=True)
    #RC_No=models.CharField(max_length=30)
    RC_Valid_Upto=models.DateField(verbose_name="RC Valid Upto in YYYY-MM-DD",null=True,blank=True)
    #Occupant_PRANAMS_ID=models.ForeignKey(Occupant_Master, on_delete=models.CASCADE)
    Insurance_Valid_Upto=models.DateField(verbose_name="Insurance Valid Upto in YYYY-MM-DD",null=True,blank=True)
    Sticker_Number_Available=models.CharField(max_length=5,choices=CHOICES)
    Existing_Sticker_Number=models.IntegerField(null=True,blank=True)
    #Entry_Extended_By=models.CharField(max_length=30)
    Remarks=models.CharField(max_length=200,null=True,blank=True)
    Updated_Date=models.DateTimeField(auto_now_add = True)
    Updated_By=models.CharField(max_length=10,default='Admin')
    Status=models.CharField(max_length=2,default='Y')
    Gate_Name=models.ManyToManyField('Gate_Master')
    def __str__(self):
        return self.Vehicle_No

# class add_vehicle_Gate_Name(models.Model):
#      Vehicle_PRANAMS_ID=models.ForeignKey(add_vehicle, on_delete=models.CASCADE)
#      Gate_ID=models.ForeignKey(Gate_Master, on_delete=models.CASCADE)
    
# class Vehicle_Gate_Map(models.Model):
#     Vehicle_PRANAMS_ID=models.ForeignKey(add_vehicle, on_delete=models.CASCADE)
#     Gate_ID=models.ForeignKey(Gate_Master, on_delete=models.CASCADE)
#     Updated_Date=models.DateField()
#     Updated_By=models.CharField(max_length=20)
#     Status=models.CharField(max_length=1)


# class add_maid(models.Model):
#     Room=models.ForeignKey(Room_Master, on_delete=models.CASCADE)
#     Maid_ID=models.IntegerField(blank=True,null=True)
#     Maid_Name=models.CharField(max_length=100, null=True, blank=True)
#     Relation=models.CharField(max_length=5, choices=RELATION_CHOICES,null=True, blank=True)
#     Relation_Name=models.CharField(max_length=100, null=True, blank=True)
#     NightDuty_Permitted=models.CharField(max_length=3,choices=CHOICES, null=True,blank=True)
#     Year_Of_Birth=models.IntegerField(null=True,blank=True)
#     Aadhaar_ID=models.IntegerField()
#     Mobile=models.IntegerField(blank=True,null=True)
#     Address_Outside_PSN=models.CharField(max_length=200, blank=True,null=True)
#     Validity=models.DateField(null=True,blank=True,verbose_name="Maid Validity in YYYY-MM-DD")
#     Remarks=models.CharField(max_length=200,null=True,blank=True)
#     Updated_Date=models.DateTimeField(auto_now_add = True)
#     Updated_By=models.CharField(max_length=10,default='Admin')
#     Status=models.CharField(max_length=2,default='Y')
    
class Emergency(models.Model):
    Room=models.ForeignKey(Room_Master, on_delete=models.CASCADE)
    Emergency_Contact_Name=models.CharField(max_length=40, blank=True,null=True)
    Emergency_Contact_Relationship=models.CharField(max_length=20, choices=RELATIONSHIP_CHOICES, blank=True,null=True)
    Emergency_Contact_ISD=models.CharField(max_length=20, blank=True,null=True)
    Emergency_Contact_Mobile_No=models.IntegerField( blank=True,null=True)
    Emergency_Contact_Email=models.CharField(max_length=40, blank=True,null=True)
    Emergency_Contact_Address=models.CharField(max_length=200, blank=True,null=True)
    Updated_Date=models.DateTimeField(auto_now_add = True)
    Updated_By=models.CharField(max_length=10,default='Admin')
    Status=models.CharField(max_length=2,default='Y')

class Maintenance(models.Model):
    Room=models.ForeignKey(Room_Master, on_delete=models.CASCADE)
    Maintenance_Charges_Paid_Upto=models.CharField(verbose_name="Maintenance Charges Paid Upto in MMM-YYYY",max_length=10,blank=True,null=True)
    Electricity_Charges_Paid_Upto=models.CharField(verbose_name="Electrical Charges Paid Upto in MMM-YYYY",max_length=10,blank=True,null=True)
    Updated_Date=models.DateTimeField(auto_now_add = True)
    Updated_By=models.CharField(max_length=10,default='Admin')
    Status=models.CharField(max_length=2,default='Y')

class VehicleTransaction(models.Model):
    Sticker_Number=models.IntegerField( blank=True,null=True)
    In_Out=models.CharField(max_length=5,null=True,blank=True)
    Updated_Date=models.DateTimeField(auto_now_add = True)
    Updated_By=models.CharField(max_length=10,default='Sevadal')
    Status=models.CharField(max_length=2,default='Y')

## Change in design for adding & updating maids
class Maid(models.Model):
    Token_Number_Available=models.CharField(max_length=5,choices=CHOICES)
    Maid_ID=models.IntegerField(unique=True)
    Maid_Name=models.CharField(max_length=100, null=True, blank=True)
    Relation=models.CharField(max_length=5, choices=RELATION_CHOICES,null=True, blank=True)
    Relation_Name=models.CharField(max_length=100, null=True, blank=True)
    NightDuty_Permitted=models.CharField(max_length=3,choices=CHOICES, null=True,blank=True)
    Year_Of_Birth=models.IntegerField(null=True,blank=True)
    Aadhaar_ID=models.IntegerField()
    Mobile=models.IntegerField(blank=True,null=True)
    Address_Outside_PSN=models.CharField(max_length=200, blank=True,null=True)
    #Validity=models.DateField(null=True,blank=True,verbose_name="Maid Validity in YYYY-MM-DD")
    Remarks=models.CharField(max_length=200,null=True,blank=True)
    Updated_Date=models.DateTimeField(auto_now_add = True)
    Updated_By=models.CharField(max_length=10,default='Admin')
    Status=models.CharField(max_length=2,default='Y')
    Room=models.ManyToManyField('Room_Master')
    Photo_File_Name=models.ImageField(upload_to="", blank=True,null=True)
    QR_Code=models.ImageField(upload_to="", blank=True,null=True)

    def __str__(self):
        return self.Maid_Name

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.Photo_File_Name))

    image_tag.short_description = 'Image'

def get_Validity():
    year=datetime.now().year
    month=datetime.now().month
    day=datetime.now().day
    date_of_last_day_of_quarter=date(2021,1,1)
    
    if(month==3 or month==6 or month==9 or month==12):
    
        if(day>=15):
            if(month==12):
                quarter=month//3
                last_month_of_quarter=3
                date_of_last_day_of_quarter = date(year+1, last_month_of_quarter, monthrange(year, last_month_of_quarter)[1])
            else:
                quarter=month//3 +1
                last_month_of_quarter = 3 * quarter
                date_of_last_day_of_quarter = date(year, last_month_of_quarter, monthrange(year, last_month_of_quarter)[1])
            
        else:
            quarter=month//3
            last_month_of_quarter = 3 * quarter
            date_of_last_day_of_quarter = date(year, last_month_of_quarter, monthrange(year, last_month_of_quarter)[1])

    else:
        quarter=month//3 +1
        last_month_of_quarter = 3 * quarter 
        date_of_last_day_of_quarter = date(year, last_month_of_quarter, monthrange(year, last_month_of_quarter)[1])

    validity=str(date_of_last_day_of_quarter)                
    return validity

class MaidTransaction(models.Model):
    Maid_ID=models.IntegerField()
    Updated_Date=models.DateTimeField(auto_now_add = True)
    Updated_By=models.CharField(max_length=10,default='Sevadal')
    In_Out=models.CharField(max_length=5,null=True,blank=True)
    Status=models.CharField(max_length=2,default='Y')


class TempVehicleTransaction(models.Model):
    Vehicle_No=models.CharField(max_length=20)
    In_Out=models.CharField(max_length=5,null=True,blank=True)
    Updated_Date=models.DateTimeField(auto_now_add = True)
    Updated_By=models.CharField(max_length=10,default='Sevadal')
    Status=models.CharField(max_length=2,default='Y')


def get_Validity():
    year=datetime.now().year
    month=datetime.now().month
    day=datetime.now().day
    date_of_last_day_of_quarter=date(2021,1,1)
    
    if(month==3 or month==6 or month==9 or month==12):
    
        if(day>=15):
            if(month==12):
                quarter=month//3
                last_month_of_quarter=3
                date_of_last_day_of_quarter = date(year+1, last_month_of_quarter, monthrange(year, last_month_of_quarter)[1])
            else:
                quarter=month//3 +1
                last_month_of_quarter = 3 * quarter
                date_of_last_day_of_quarter = date(year, last_month_of_quarter, monthrange(year, last_month_of_quarter)[1])
            
        else:
            quarter=month//3
            last_month_of_quarter = 3 * quarter
            date_of_last_day_of_quarter = date(year, last_month_of_quarter, monthrange(year, last_month_of_quarter)[1])

    else:
        quarter=month//3 +1
        last_month_of_quarter = 3 * quarter 
        date_of_last_day_of_quarter = date(year, last_month_of_quarter, monthrange(year, last_month_of_quarter)[1])

    validity=str(date_of_last_day_of_quarter)                
    return validity

class maid_renewal(models.Model):
    Maid_ID=models.ForeignKey(Maid, on_delete=models.CASCADE)
    Maid_ID=models.IntegerField()
    Validity=models.DateField(default=get_Validity)
    Updated_Date=models.DateTimeField(auto_now_add = True)
    Updated_By=models.CharField(max_length=10,default='CSO')
    Status=models.CharField(max_length=2,default='Y')

class vehicle_renewal(models.Model):
    Sticker_Num=models.IntegerField()
    Validity=models.DateField(default=get_Validity)
    Updated_Date=models.DateTimeField(auto_now_add = True)
    Updated_By=models.CharField(max_length=10,default='CSO')
    Status=models.CharField(max_length=2,default='Y')


class TempVehicle(models.Model):
     Vehicle_No=models.CharField(max_length=20,unique=True)
     Name=models.CharField(max_length=100,null=True,blank=True)
     Type_Of_Vehicle=models.CharField(max_length=20, choices=VEHICLE_TYPE_CHOICES)
     Purpose=models.CharField(max_length=100,null=True,blank=True)
     Reference_Person_in_Ashram=models.CharField(max_length=100)
     Date_in=models.DateField(default=datetime.now().date() + timedelta(days=1))
     Date_out=models.DateField(default=datetime.now().date() + timedelta(days=2))
     Remarks=models.CharField(max_length=100,null=True,blank=True)
     Updated_Date=models.DateTimeField(auto_now_add = True)
     Updated_By=models.CharField(max_length=10,default='CSO')
     Status=models.CharField(max_length=2,default='Y') 

    
# class MyModel(models.Model):
#     my_state_field = StateField()    
    
# class search_Room_transaction(models.Model):
#     Room=models.ForeignKey(Room_Master, on_delete=models.CASCADE, blank=True,null=True)



