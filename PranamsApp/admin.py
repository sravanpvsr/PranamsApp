from django.contrib import admin
from .models import *

admin.site.site_header="PRANAMS Administration"


class DemographyAdmin(admin.ModelAdmin):
    list_display=('Room','Category','Name','Mobile','Sub_Division_Name','image_tag','my_state_field')
    search_fields=["Room__Room","Name"]#,'Category')
    filter_horizontal=()
    list_filter=('Category','Institution_Name','Sub_Division_Name','Blood_Group')
    fieldsets=()
    

    #fields = ['image_tag']

class EmergencyAdmin(admin.ModelAdmin):
    list_display=('Room','Emergency_Contact_Name','Emergency_Contact_Relationship','Emergency_Contact_ISD','Emergency_Contact_Mobile_No','Emergency_Contact_Email')
    search_fields=["Room__Room","Emergency_Contact_Name"]#,'Category')
    filter_horizontal=()
    list_filter=('Emergency_Contact_Relationship','Emergency_Contact_ISD')
    fieldsets=()

# class MaidAdmin(admin.ModelAdmin):
#     list_display=('Room','Maid_ID','Maid_Name','Relation_Name','NightDuty_Permitted','Mobile')
#     search_fields=["Room__Room","Maid_ID",'Maid_Name']#,'Category')
#     filter_horizontal=()
#     list_filter=['NightDuty_Permitted']
#     fieldsets=()

class MaintenanceAdmin(admin.ModelAdmin):
    list_display=('Room','Maintenance_Charges_Paid_Upto','Electricity_Charges_Paid_Upto')
    search_fields=["Room__Room"]#,'Category')
    filter_horizontal=()
    list_filter=("Maintenance_Charges_Paid_Upto",'Electricity_Charges_Paid_Upto')
    fieldsets=()

class VehicleAdmin(admin.ModelAdmin):
    list_display=('Room','Member_Name','Vehicle_No','Two_Four_Wheeler','Existing_Sticker_Number')
    search_fields=["Room",'Member_Name','Vehicle_No','Existing_Sticker_Number']#,'Category')
    filter_horizontal=()
    list_filter=['Two_Four_Wheeler']
    fieldsets=()

class MaidAdmin(admin.ModelAdmin):
    list_display=('rooms','Maid_ID','Maid_Name','Relation_Name','NightDuty_Permitted','Mobile','image_tag')
    search_fields=["Room__Room","Maid_ID",'Maid_Name']#,'Category')
    filter_horizontal=()
    list_filter=['NightDuty_Permitted']
    fieldsets=()

    def rooms(self, obj):
        return ", ".join([r.Room for r in obj.Room.all()])

class TempVehicleAdmin(admin.ModelAdmin):
    list_display=('Vehicle_No','Type_Of_Vehicle','Purpose','Reference_Person_in_Ashram','Date_in','Date_out')
    search_fields=["Vehicle_No",'Date_in','Date_out']#,'Category')
    filter_horizontal=()
    list_filter=['Type_Of_Vehicle']
    fieldsets=()

# Register your models here.
admin.site.register(Demography,DemographyAdmin
)
#admin.site.register(add_maid,MaidAdmin)
admin.site.register(Emergency,EmergencyAdmin)
admin.site.register(Maintenance,MaintenanceAdmin)
admin.site.register(Vehicle,VehicleAdmin)      
admin.site.register(Maid,MaidAdmin)                
admin.site.register(TempVehicle,TempVehicleAdmin)