from rest_framework import serializers
from PranamsApp.models import Member_Category_Master,Institution_Master,Sub_Division_Master,Institution_Sub_Division_Map,Room_Type_Master,Room_Master,Gate_Master

class Member_Category_Master_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Member_Category_Master
        fields=('Member_Category_ID',
        'Member_Category',
        'Updated_Date',
        'Updated_By',
        'Status')

class Institution_Master_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Institution_Master
        fields=('Institution_ID',
        'Institution_Name',
        'Updated_Date',
        'Updated_By',
        'Status')
    
class Sub_Division_Master_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_Division_Master
        fields=('Sub_Division_ID',
        'Sub_Division_Name',
        'Updated_Date',
        'Updated_By',
        'Status')

class Institution_Sub_Division_Map_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Institution_Sub_Division_Map
        fields=('Institution_ID',
        'Sub_Division_ID',
        'Updated_Date',
        'Updated_By',
        'Status')

# class Member_Master_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Member_Master
#         fields=('Member_PRANAMS_ID',
#         'Member_Name',
#         'Member_Photo_File_Name',
#         'Member_Type',
#         'Member_Aadhaar_ID',
#         'Member_Photo',
#         'Member_DOB',
#         'Member_Mobile',
#         'Member_Whatsapp',
#         'Member_Blood_Group',
#         'Staff_Institution_ID',
#         'Staff_Sub_Division_ID',
#         'Staff_Designation',
#         'Staff_Working_Since',
#         'Staff_Institutuon_Emp_ID',
#         'Updated_Date',
#         'Updated_By',
#         'Status',
#         'Member_Category_ID',
#         'Address_Outside_PSN',
#         'Emergency_Contact_Name',
#         'Emergency_Contact_Email',
#         'Emergency_Contact_Relationship',
#         'Emergency_Contact_ISD',
#         'Emergency_Contact_Mobile_No',
#         'Emergency_Contact_Address',
#         'Member_DL_Validity')

class Room_Type_Master_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Room_Type_Master
        fields=('Room_Type_ID',
        'Room_Type_Desc',
        'Updated_Date',
        'Updated_By',
        'Status')

class Room_Master_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Room_Master
        fields=('Room',
        'Room_Type_ID',
        'Updated_Date',
        'Updated_By',
        'Status')

# class Member_Accommodation_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Member_Accommodation
#         fields=('Member_PRANAMS_ID',
#         'Room',
#         'Updated_Date',
#         'Updated_By',
#         'Status')

# class Occupant_Master_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Occupant_Master
#         fields=('Member_PRANAMS_ID',
#         'Occ_Name',
#         'Occ_DOB',
#         'Occ_Relationship',
#         'Occ_Permanent_Resident_Not',
#         'Occ_Aadhaar_ID',
#         'Occupant_PRANAMS_ID',
#         'Occ_DL_No',
#         'Status',
#         'Updated_Date',
#         'Updated_By',
#         'Status')

# class Vehicle_Master_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Vehicle_Master
#         fields=('Member_PRANAMS_ID',
#         'Vehicle_PRANAMS_ID',
#         'Vehicle_No',
#         'Two_Four_Wheeler',
#         'RC_No',
#         'RC_Valid_Upto',
#         'Occupant_PRANAMS_ID',
#         'Insurance_Valid_Upto',
#         'Entry_Extended_By',
#         'Remarks',
#         'Updated_Date',
#         'Updated_By',
#         'Status')

class Gate_Master_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Gate_Master
        fields=('Gate_ID',
        'Gate_Name',
        'Updated_Date',
        'Updated_By',
        'Status')

# class Vehicle_Gate_Map_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Vehicle_Gate_Map
#         fields=('Vehicle_PRANAMS_ID',
#         'Gate_ID',
#         'Updated_Date',
#         'Updated_By',
#         'Status')