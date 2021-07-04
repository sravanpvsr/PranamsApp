from django.db import models

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



class Member_Master(models.Model):
    Member_PRANAMS_ID=models.CharField(primary_key=True,max_length=20)
    Member_Name=models.CharField(max_length=100)   
    Member_Photo_File_Name=models.CharField(max_length=150)
    #Member_Type=models.CharField(max_length=20)
    Member_Aadhaar_ID=models.IntegerField()
    Member_DOB=models.DateField()
    Member_Mobile=models.IntegerField()
    Member_Whatsapp=models.IntegerField()
    Member_Blood_Group=models.CharField(max_length=10)
    #Staff_Institution_ID=models.ForeignKey(Institution_Master, on_delete=models.CASCADE)
    #Staff_Sub_Division_ID=models.ForeignKey(Sub_Division_Master, on_delete=models.CASCADE)
    Staff_Designation=models.CharField(max_length=20)
    Staff_Working_Since=models.DateField()
    #Staff_Institution_Emp_ID=models.CharField(max_length=20)
    Updated_Date=models.DateField()
    Updated_By=models.CharField(max_length=20)
    Status=models.CharField(max_length=1)
    #Member_Category_ID=models.ForeignKey(Member_Category_Master, on_delete=models.CASCADE)
    Address_Outside_PSN=models.CharField(max_length=200)
    Emergency_Contact_Name=models.CharField(max_length=40)
    Emergency_Contact_Email=models.CharField(max_length=40)
    Emergency_Contact_Relationship=models.CharField(max_length=20)
    Emergency_Contact_ISD=models.CharField(max_length=20)
    Emergency_Contact_Mobile_No=models.IntegerField()
    Emergency_Contact_Address=models.CharField(max_length=200)
    #Member_DL_No=models.CharField(max_length=50)
    #Member_DL_Validity=models.DateField()

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


class Member_Accommodation(models.Model):
    Member_PRANAMS_ID=models.ForeignKey(Member_Master, on_delete=models.CASCADE)
    Room=models.ForeignKey(Room_Master, on_delete=models.CASCADE)
    Updated_Date=models.DateField()
    Updated_By=models.CharField(max_length=20)
    Status=models.CharField(max_length=1)


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
    ('member','Member'),
    ('occupant','Occupant')
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

class Occupant_Master(models.Model):
    Occ_ID=models.IntegerField(primary_key=True)
    Room=models.ForeignKey(Room_Master, on_delete=models.CASCADE)
    Staff_Choice = models.CharField(max_length=5, choices=CHOICES)     
    #Room_Type=models.ForeignKey(Room_Type_Master, on_delete=models.CASCADE, blank=True)
    Name=models.CharField(max_length=100)
    DOB=models.DateField()
    Aadhaar_ID=models.IntegerField()
    Relationship_With_Primary_Member=models.CharField(max_length=20, choices=RELATIONSHIP_CHOICES)
    Permanent_Resident_Or_Not=models.CharField(blank=True,max_length=5, choices=CHOICES)
    Blood_Group=models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES,blank=True)
    Occupant_Category=models.ForeignKey(Member_Category_Master, on_delete=models.CASCADE,blank=True)
    Institution_Name=models.ForeignKey(Institution_Master, on_delete=models.CASCADE, blank=True)
    Sub_Division_Name=models.ForeignKey(Sub_Division_Master, on_delete=models.CASCADE, blank=True)
    Staff_Working_Since=models.DateField(blank=True)
    Staff_Designation=models.CharField(max_length=50, blank=True)
    Staff_Institution_Emp_ID=models.CharField(max_length=20, blank=True)
    Mobile=models.IntegerField(blank=True)
    Whatsapp_Choice = models.CharField(max_length=5, choices=CHOICES, blank=True)
    Whatsapp=models.IntegerField(blank=True)
    Photo_File_Name=models.CharField(max_length=150,blank=True)  
    #Staff_Choice = models.CharField(max_length=5, choices=CHOICES)     
    #Member_DL_No=models.CharField(max_length=50)
    #Member_DL_Validity=models.DateField()    
    #Address_Outside_PSN=models.CharField(max_length=200, blank=True)
    Emergency_Contact_Name=models.CharField(max_length=40,blank=True)
    Emergency_Contact_Email=models.CharField(max_length=40,blank=True)
    Emergency_Contact_Relationship=models.CharField(max_length=20, choices=RELATIONSHIP_CHOICES,blank=True)
    Emergency_Contact_ISD=models.CharField(max_length=20,blank=True)
    Emergency_Contact_Mobile_No=models.IntegerField(blank=True)
    Emergency_Contact_Address=models.CharField(max_length=200,blank=True)
    Updated_Date=models.DateTimeField(auto_now_add = True)
    Updated_By=models.CharField(max_length=10,default='Admin')
    Status=models.CharField(max_length=2,default='Y')

class add_demography(models.Model):
    Member_Category=models.ForeignKey(Member_Category_Master, on_delete=models.CASCADE)
    Room=models.ForeignKey(Room_Master, on_delete=models.CASCADE, blank=True)
    Room_Type=models.ForeignKey(Room_Type_Master, on_delete=models.CASCADE, blank=True)
    Member_Name=models.CharField(max_length=100)
    Member_DOB=models.DateField()
    Member_Blood_Group=models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    Institution_Name=models.ForeignKey(Institution_Master, on_delete=models.CASCADE, blank=True)
    Sub_Division_Name=models.ForeignKey(Sub_Division_Master, on_delete=models.CASCADE, blank=True)
    Staff_Working_Since=models.DateField(blank=True)
    Staff_Designation=models.CharField(max_length=50, blank=True)
    Staff_Institution_Emp_ID=models.CharField(max_length=20, blank=True)
    Member_Mobile=models.IntegerField()
    Whatsapp_Choice = models.CharField(max_length=5, choices=CHOICES)
    Member_Whatsapp=models.IntegerField(blank=True)
    Member_Photo_File_Name=models.CharField(max_length=150)  
    #Staff_Choice = models.CharField(max_length=5, choices=CHOICES)     
    Member_Aadhaar_ID=models.IntegerField()
    #Member_DL_No=models.CharField(max_length=50)
    #Member_DL_Validity=models.DateField()    
    Address_Outside_PSN=models.CharField(max_length=200, blank=True)
    Emergency_Contact_Name=models.CharField(max_length=40)
    Emergency_Contact_Email=models.CharField(max_length=40)
    Emergency_Contact_Relationship=models.CharField(max_length=20, choices=RELATIONSHIP_CHOICES)
    Emergency_Contact_ISD=models.CharField(max_length=20)
    Emergency_Contact_Mobile_No=models.IntegerField()
    Emergency_Contact_Address=models.CharField(max_length=200)
    Updated_Date=models.DateTimeField(auto_now_add = True)
    Updated_By=models.CharField(max_length=10,default='Admin')
    Status=models.CharField(max_length=2,default='Y')

class add_vehicle(models.Model):
    Room=models.ForeignKey(Room_Master, on_delete=models.CASCADE)
    Vehicle_Available=models.CharField(max_length=3, choices=CHOICES)
    Member_Occupant=models.CharField(max_length=15,choices=MEMBER_CHOICES)
    #Member_Name=models.ForeignKey(Member_Master,on_delete=models.CASCADE)
    #Member_PRANAMS_ID=models.ForeignKey(Member_Master, on_delete=models.CASCADE)
    #Occupant_Name=models.ForeignKey(Occupant_Master, on_delete=models.CASCADE)
    #Vehicle_PRANAMS_ID=models.CharField(primary_key=True,max_length=10)
    DL_No=models.CharField(max_length=50)
    DL_Validity=models.DateField()
    Two_Four_Wheeler=models.CharField(max_length=5,choices=TWO_FOUR_WHEELER)
    Vehicle_No=models.CharField(max_length=20)
    RC_No=models.CharField(max_length=30)
    RC_Valid_Upto=models.DateField()
    #Occupant_PRANAMS_ID=models.ForeignKey(Occupant_Master, on_delete=models.CASCADE)
    Insurance_Valid_Upto=models.DateField()
    #Entry_Extended_By=models.CharField(max_length=30)
    Remarks=models.CharField(max_length=200)
    Updated_Date=models.DateTimeField(auto_now_add = True)
    Updated_By=models.CharField(max_length=20)
    Status=models.CharField(max_length=1)
    Gate_Name=models.ManyToManyField('Gate_Master')
    

    def __str__(self):
        return self.name
    

class Vehicle_Gate_Map(models.Model):
    Vehicle_PRANAMS_ID=models.ForeignKey(add_vehicle, on_delete=models.CASCADE)
    Gate_ID=models.ForeignKey(Gate_Master, on_delete=models.CASCADE)
    Updated_Date=models.DateField()
    Updated_By=models.CharField(max_length=20)
    Status=models.CharField(max_length=1)









