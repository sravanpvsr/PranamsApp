from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
import  datetime
from .filters import *
from django.db.models import Value, Max
from calendar import monthrange
import calendar
from datetime import datetime
from datetime import date
from django import forms

from PranamsApp.models import *
from PranamsApp.serializers import Member_Category_Master_Serializer,Institution_Master_Serializer,Sub_Division_Master_Serializer,Institution_Sub_Division_Map_Serializer,Room_Type_Master_Serializer,Room_Master_Serializer,Gate_Master_Serializer
from PranamsApp.forms import *
from django.contrib.auth import authenticate,logout as deauth, login  as dj_login
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required,user_passes_test




# Create your views here.  

def is_staff(user):
    return user.is_staff

@csrf_exempt



# For HTML
def home(request):
    return render(request,"home.html")


@login_required
@user_passes_test(is_staff)
def demography(request):
    
    # displayMemberCategory=Member_Category_Master.objects.all()
    # displayRoom=Room_Master.objects.all()
    # displayInstitution=Institution_Master.objects.all()
    # displaySubDivision=Institution_Sub_Division_Map.objects.all()
    # displayRoomType=Room_Type_Master.objects.all()
    context={}
    form=add_demography_form()

    if request.method=="POST":
        form=add_demography_form(request.POST,request.FILES)
        if form.is_valid():
            data=form.save()
            #data=form.save(commit=FALSE)
            #data.save()
            context["status"]="{} Added Successfully".format(data.Name)
        else:
            context["errorStatus"]="Please correct the errors and re-submit"
            #return render(request, "demography.html", {'form':form})

    context["form"] =form

    return render(request,"demography.html",
    context)
    
    # {"Member_Category_Master":displayMemberCategory,
    # "Room_Master":displayRoom,
    # "Institution_Master":displayInstitution,
    # "Sub_Division_Master":displaySubDivision,
    # "Room_Type_Master":displayRoomType
    # }
    #)

@login_required
@user_passes_test(is_staff)
def occupant(request):
    context={}
    occ_form=add_occupant_form()

    if request.method=="POST":
        occ_form=add_occupant_form(request.POST,request.FILES)
        if occ_form.is_valid():
            data=occ_form.save()
            #data=form.save(commit=FALSE)
            #data.save()
            context["status"]="{} Added Successfully. In case there are more occupants, please fill the form again".format(data.Name)
        else:
            context["errorStatus"]="Please correct the mistakes and re-submit"
            #return render(request, "demography.html", {'form':form})

    context["occ_form"] =occ_form

    return render(request,"occupant.html",
    context)
    
#Updated - 8-Jul-2021
@login_required
@user_passes_test(is_staff)
def vehicle(request):
    room_id=request.GET.get('Room')
    Member_Occupant=request.GET.get('Member_Occupant')

    sat=Demography.objects.filter(Room=room_id, Status='Y')
    print(sat)
    m_names=[]
    o_names=[]
    if sat:
        for s in sat:
            if Member_Occupant == 'member':
                if not s.Member_Occupant:
                    m_names.append(s.Name)
                    print(m_names)
                else:
                    pass
            if Member_Occupant == 'occupant':
                if s.Member_Occupant:
                    o_names.append(s.Name)
                else:
                    pass    
   
    if room_id:
        if m_names != []:
        
            your_list_as_json = json.dumps(m_names)
            print(your_list_as_json)
            return HttpResponse(your_list_as_json ,content_type ="application/json")
        else:

            your_list_as_json = json.dumps(o_names)
            print(your_list_as_json)
            return HttpResponse(your_list_as_json ,content_type ="application/json")                

    context={}
    vehicle_form=add_vehicle_form()                  
    #print(obj,sat)
    # if request.method=='GET':
    #     institution = Institution_Master.objects.all()
    #     institution_serializer = Institution_Master_Serializer(institution, many=True)
    #     return JsonResponse(institution_serializer.data, safe=False)
    
    if request.method=="POST":
        Type_Of_Owner=request.POST.get('Type_Of_Owner')
        Owner_Name=''
        if Type_Of_Owner=='ashramResident':
            Room=request.POST.get('Room')
            print(Room)
            print('here')
            Member_Occupant=request.POST.get('Member_Occupant')
            Member_Name=request.POST.get('Member_Name')
            memberinstance=Demography.objects.get(Name=Member_Name)
        else:
            Room='ZEXCL' #Used for outside Ashram vehicles
            Member_Occupant=''
            Member_Name='OutsideAshram'
            memberinstance=Demography.objects.get(Name=Member_Name)
            Owner_Name=request.POST.get('Owner_Name')       
        Roominstance=Room_Master.objects.get(Room=Room) 
        Vehicle_Available=request.POST.get('Vehicle_Available')
        DL_No=request.POST.get('DL_No')
        DL_Validity=request.POST.get('DL_Validity')
        Two_Four_Wheeler=request.POST.get('Two_Four_Wheeler')
        Vehicle_No=request.POST.get('Vehicle_No')
        #RC_No=request.POST.get('RC_No')
        RC_Valid_Upto=request.POST.get('RC_Valid_Upto')
        Insurance_Valid_Upto=request.POST.get('Insurance_Valid_Upto')
        Remarks=request.POST.get('Remarks')
        Gate_Name=request.POST.getlist('Gate_Name')
        Existing_Sticker_Number=request.POST.get('Existing_Sticker_Number')
        
        
        
        if not Existing_Sticker_Number:
            max_sticker_no = (
            Vehicle.objects
           .annotate(common=Value(1))
           .values('common')
           .annotate(max_sticker_num=Max('Existing_Sticker_Number'))
           .values('max_sticker_num')
            )
        

            for n in max_sticker_no:
                max_sticker_no=n['max_sticker_num']

            Existing_Sticker_Number=max_sticker_no+1

        # print(Room,Vehicle_Available,Member_Occupant,Member_Name,DL_No,DL_Validity,Two_Four_Wheeler,
        #     Vehicle_No,RC_Valid_Upto,Insurance_Valid_Upto,Remarks,Gate_Name)            
        vehicle_details=Vehicle(
                Type_Of_Owner=Type_Of_Owner,
                Room=Roominstance,
                Member_Occupant=Member_Occupant,
                Member_Name=memberinstance,
                DL_No=DL_No,
                DL_Validity=DL_Validity,
                Two_Four_Wheeler=Two_Four_Wheeler,
                Vehicle_No=Vehicle_No,
                RC_Valid_Upto=RC_Valid_Upto,
                Insurance_Valid_Upto=Insurance_Valid_Upto,
                Remarks=Remarks,
                Existing_Sticker_Number=Existing_Sticker_Number,
                Owner_Name=Owner_Name

            )

        
        vehicle_details.save()
        vehicle_details.Gate_Name.add(*Gate_Name)
        context["status"]="Vehicle with Sticker No. {} added Successfully.".format(Existing_Sticker_Number)

    context["vehicle_form"] =vehicle_form 

    return render(request,"vehicle.html",
    context)

@login_required
def searchVehicle(request):
    
    veh=Vehicle.objects.filter(Status='Y')

    vehFilter=VehicleFilter(request.GET,queryset=veh)
    veh=vehFilter.qs
    
    # filter(Vehicle_No=vehicle_num, Status='Y')
    context={'data':veh,'vehFilter':vehFilter}


    return render(request,"searchVehicle.html",
    context)

# @login_required
# def searchMaid(request):    
#     maid=Maid.objects.filter(Status='Y')
#     maidFilter=MaidFilter(request.GET,queryset=maid)
#     maid=maidFilter.qs
#     # filter(Vehicle_No=vehicle_num, Status='Y')
#     context={'data':maid,'maidFilter':maidFilter}

#     return render(request,"searchMaid.html",
#     context)

@login_required
def searchMaidRenewal(request):

    year=datetime.now().year
    month=datetime.now().month
    day=datetime.now().day
    
    date_of_last_day_of_quarter=datetime(2021,1,1)
    
    if(month==3 or month==6 or month==9 or month==12):    
        if(day>=15):
            if(month==12):
                quarter=month//3
                last_month_of_quarter=3
                date_of_last_day_of_quarter = datetime(year+1, last_month_of_quarter, monthrange(year, last_month_of_quarter)[1])
            else:
                quarter=month//3 +1
                last_month_of_quarter = 3 * quarter
                date_of_last_day_of_quarter = datetime(year, last_month_of_quarter, monthrange(year, last_month_of_quarter)[1])
            
        else:
            quarter=month//3
            last_month_of_quarter = 3 * quarter
            date_of_last_day_of_quarter = datetime(year, last_month_of_quarter, monthrange(year, last_month_of_quarter)[1])

    else:
        quarter=month//3 +1
        last_month_of_quarter = 3 * quarter 
        date_of_last_day_of_quarter = datetime(year, last_month_of_quarter, monthrange(year, last_month_of_quarter)[1])

    validity_date=date_of_last_day_of_quarter.date()
    print(validity_date)
    maid=maid_renewal.objects.filter(Status='Y').exclude(Validity='2012-12-31')
    maidRenewalFilter=MaidRenewalFilter(request.GET,queryset=maid)
    maid=maidRenewalFilter.qs

    # filter(Vehicle_No=vehicle_num, Status='Y')
    context={'data':maid,'maidRenewalFilter':maidRenewalFilter}

    return render(request,"searchMaidRenewal.html",
    context)

@login_required
def searchRoomCompact(request):
    
    dem=Demography.objects.filter(Status='Y')

    demFilter=RoomFilter(request.GET,queryset=dem)
    dem=demFilter.qs

    
    
    # filter(Vehicle_No=vehicle_num, Status='Y')
    context={'data':dem,'demFilter':demFilter}


    return render(request,"searchRoomCompact.html",
    context)

@login_required
def searchTempVehicle(request):
    
    tv=TempVehicle.objects.filter(Status='Y')

    tvFilter=TempVehicleFilter(request.GET,queryset=tv)
    tv=tvFilter.qs

    
    
    # filter(Vehicle_No=vehicle_num, Status='Y')
    context={'data':tv,'tvFilter':tvFilter}


    return render(request,"searchTempVehicle.html",
    context)

@login_required
def searchRoom(request):
    room=request.GET.get('Room')
    your_list_as_json={}
    
    # if maidID is not None:
    #     maidID=int(maidID)

    sat=Demography.objects.filter(Room=room, Status='Y',
    Member_Occupant = None)

    
    sat1=Demography.objects.filter(Room=room, Status='Y',
    Member_Occupant__isnull=False)
    print(sat1)

    sat2=Vehicle.objects.filter(Room=room,Status='Y')
   

    sat3=Maid.objects.filter(
        Room=room, Status='Y')
    
    
    
    p_name=[]
    p_staff=[]
    p_category=[]
    p_room_type=[]
    p_room=[]
    p_age=[]
    p_mobile=[]
    p_aadhaar=[]
    p_whatsapp=[]
    p_landline_num=[]
    p_email=[]
    p_bloodgroup=[]
    p_SSSIHMS_PG_Patient_ID=[]
    p_Institution_Name=[]
    p_Sub_Division_Name=[]
    p_Staff_Working_Since=[]
    p_Staff_Institution_Emp_ID=[]
    p_Remarks=[]
    p_photo=[]

    p_name1=[]
    p_staff1=[]
    p_category1=[]
    p_room_type1=[]
    p_room1=[]
    p_age1=[]
    p_mobile1=[]
    p_aadhaar1=[]
    p_whatsapp1=[]
    p_landline_num1=[]
    p_email1=[]
    p_bloodgroup1=[]
    p_SSSIHMS_PG_Patient_ID1=[]
    p_Institution_Name1=[]
    p_Sub_Division_Name1=[]
    p_Staff_Working_Since1=[]
    p_Staff_Institution_Emp_ID1=[]
    p_Remarks1=[]
    p_photo1=[]

    p_dl_no=[]
    p_dl_validity=[]
    p_two_four_wheeler=[]
    p_vehicle_no=[]
    p_rc_validity=[]
    p_insurance_validity=[]
    p_remarks2=[]
    p_existing_sticker_number=[]

    p_maid_id=[]
    p_maid_name=[]
    p_rel=[]
    p_rel_name=[]
    p_nd=[]
    p_aadhaar3=[]
    p_mobile3=[]
    p_address3=[]
    p_remarks3=[]
    p_photo3=[]
    p_maid_validity=[]
    p_dob3=[]

    
    if sat:
        for s in sat: 
            p_name.append(str.upper(s.Name))
            if not s.Member_Occupant:
                s.Member_Occupant='Staff'
            p_staff.append(str.upper(s.Member_Occupant))

            p_category.append(s.Category)
            p_room_type.append(s.Room_Type)
            p_room.append(s.Room)

            dob_original_date = datetime.datetime.strptime(str(s.DOB), '%Y-%m-%d')
            #dob_formatted_date = dob_original_date.strftime("%d-%m-%Y")
            today=datetime.date.today()
            p_age.append(today.year-dob_original_date.year)
            
            p_mobile.append(s.Mobile)
            p_aadhaar.append(s.Aadhaar_ID)
            p_whatsapp.append(s.Whatsapp)
            p_landline_num.append(s.Landline_Number)
            if(s.Email):
                p_email.append(str.upper(s.Email))
            if(s.Blood_Group):
                p_bloodgroup.append(str.upper(s.Blood_Group))
            if(s.SSSIHMS_PG_Patient_ID):
                p_SSSIHMS_PG_Patient_ID.append(str.upper(s.SSSIHMS_PG_Patient_ID))
            if(s.Institution_Name):
                p_Institution_Name.append(s.Institution_Name)
            if(s.Sub_Division_Name):
                p_Sub_Division_Name.append(s.Sub_Division_Name)

            if(s.Staff_Working_Since):
                ws_original_date=datetime.datetime.strptime(str(s.Staff_Working_Since), '%Y-%m-%d')
                ws_formatted_date=ws_original_date.strftime("%d-%m-%Y")
                p_Staff_Working_Since.append(str(ws_formatted_date))

            if(s.Staff_Institution_Emp_ID):
                p_Staff_Institution_Emp_ID.append(str.upper(s.Staff_Institution_Emp_ID))
            
            p_Remarks.append(s.Remarks)
            
            if(s.Photo_File_Name):
                p_photo.append(str(s.Photo_File_Name))
            
        
        your_list_as_json["Name"]=p_name
        your_list_as_json["Member_Occupant"]=p_staff
        your_list_as_json["Category"]=str(p_category[0])
        your_list_as_json["Room_Type"]=str(p_room_type[0])
        your_list_as_json["Room"]=str(p_room[0])
        your_list_as_json["DOB"]=str(p_age)+" years"
        your_list_as_json["Mobile"]=p_mobile
        your_list_as_json["Aadhaar_ID"]=p_aadhaar
        your_list_as_json["Whatsapp"]=p_whatsapp
        your_list_as_json["Landline_Number"]=p_landline_num
        your_list_as_json["Email"]=p_email
        your_list_as_json["Blood_Group"]=p_bloodgroup
        your_list_as_json["SSSIHMS_PG_Patient_ID"]=p_SSSIHMS_PG_Patient_ID
        if(p_Institution_Name):
            your_list_as_json["Institution_Name"]=str(p_Institution_Name[0])
        if(p_Sub_Division_Name):
            your_list_as_json["Sub_Division_Name"]=str(p_Sub_Division_Name[0])
        your_list_as_json["Staff_Working_Since"]=p_Staff_Working_Since
        your_list_as_json["Staff_Institution_Emp_ID"]=p_Staff_Institution_Emp_ID
        your_list_as_json["Remarks"]=p_Remarks
        your_list_as_json["Photo_File_Name"]=p_photo
        


        if sat1:
            for s in sat1: 
                p_name1.append(str.upper(s.Name))
                if s.Member_Occupant=='member':
                    s.Member_Occupant='Staff'
                p_staff1.append(str.upper(s.Member_Occupant))

                p_category1.append(s.Category)
                

                dob_original_date1 = datetime.datetime.strptime(str(s.DOB), '%Y-%m-%d')
            #dob_formatted_date = dob_original_date.strftime("%d-%m-%Y")
                today=datetime.date.today()
                p_age1.append(today.year-dob_original_date1.year)
            
                p_mobile1.append(s.Mobile)
                p_aadhaar1.append(s.Aadhaar_ID)
                p_whatsapp1.append(s.Whatsapp)
                p_landline_num1.append(s.Landline_Number)
                if(s.Email):
                    p_email1.append(str.upper(s.Email))
                if(s.Blood_Group):
                    p_bloodgroup1.append(str.upper(s.Blood_Group))
                if(s.SSSIHMS_PG_Patient_ID):
                    p_SSSIHMS_PG_Patient_ID1.append(str.upper(s.SSSIHMS_PG_Patient_ID))
                if(s.Institution_Name):
                    p_Institution_Name1.append(s.Institution_Name)
                if(s.Sub_Division_Name):
                    p_Sub_Division_Name1.append(s.Sub_Division_Name)

                if(s.Staff_Working_Since):
                    ws_original_date=datetime.datetime.strptime(str(s.Staff_Working_Since), '%Y-%m-%d')
                    ws_formatted_date=ws_original_date.strftime("%d-%m-%Y")
                    p_Staff_Working_Since1.append(str(ws_formatted_date))

                if(s.Staff_Institution_Emp_ID):
                    p_Staff_Institution_Emp_ID1.append(str.upper(s.Staff_Institution_Emp_ID))
            
                p_Remarks1.append(s.Remarks)
            
                if(s.Photo_File_Name):
                    p_photo1.append(str(s.Photo_File_Name))
            
                
        your_list_as_json["Name1"]=p_name1
        your_list_as_json["Member_Occupant1"]=p_staff1
        
        if(p_category1):
            your_list_as_json["Category1"]=str(p_category1[0])
        
        your_list_as_json["DOB1"]=str(p_age1)+" years"
        your_list_as_json["Mobile1"]=p_mobile1
        your_list_as_json["Aadhaar_ID1"]=p_aadhaar1
        your_list_as_json["Whatsapp1"]=p_whatsapp1
        your_list_as_json["Landline_Number1"]=p_landline_num1
        your_list_as_json["Email1"]=p_email1
        your_list_as_json["Blood_Group1"]=p_bloodgroup1
        your_list_as_json["SSSIHMS_PG_Patient_ID1"]=p_SSSIHMS_PG_Patient_ID1
        if(p_Institution_Name1):
            your_list_as_json["Institution_Name1"]=str(p_Institution_Name1[0])
        if(p_Sub_Division_Name1):
            your_list_as_json["Sub_Division_Name1"]=str(p_Sub_Division_Name1[0])
        your_list_as_json["Staff_Working_Since1"]=p_Staff_Working_Since1
        your_list_as_json["Staff_Institution_Emp_ID1"]=p_Staff_Institution_Emp_ID1
        your_list_as_json["Remarks1"]=p_Remarks1
        your_list_as_json["Photo_File_Name1"]=p_photo1
        

        if sat2:
            for s in sat2: 
                p_vehicle_no.append(str.upper(s.Vehicle_No))
                p_existing_sticker_number.append(s.Existing_Sticker_Number)
                p_two_four_wheeler.append(str.upper(s.Two_Four_Wheeler))
                p_dl_no.append(str.upper(s.DL_No))
                
                p_dl_validity_original = datetime.datetime.strptime(str(s.DL_Validity), '%Y-%m-%d')
                dl_formatted_date=p_dl_validity_original.strftime("%d-%m-%Y")
                p_dl_validity.append(str(dl_formatted_date))
                
                p_rc_validity_original = datetime.datetime.strptime(str(s.RC_Valid_Upto), '%Y-%m-%d')
                rc_formatted_date=p_rc_validity_original.strftime("%d-%m-%Y")
                p_rc_validity.append(str(rc_formatted_date))
                
                p_ins_validity_original = datetime.datetime.strptime(str(s.Insurance_Valid_Upto), '%Y-%m-%d')
                ins_formatted_date=p_ins_validity_original.strftime("%d-%m-%Y")
                p_insurance_validity.append(str(ins_formatted_date))

                p_remarks2.append(s.Remarks)
        
        your_list_as_json["Vehicle2"]=p_vehicle_no
        your_list_as_json["Existing_Sticker_Number2"]=p_existing_sticker_number
        your_list_as_json["Two_Four_Wheeler2"]=str(p_two_four_wheeler)
        
        your_list_as_json["DL_No2"]=p_dl_no
        your_list_as_json["RC_Valid_Upto2"]=p_rc_validity
        your_list_as_json["DL_Validity2"]=p_dl_validity
        your_list_as_json["Insurance_Valid_Upto2"]=p_insurance_validity       
        your_list_as_json["Remarks2"]=p_remarks2  

        if sat3:
            for s in sat3: 
                p_maid_id.append(s.Maid_ID)
                p_maid_name.append(str.upper(s.Maid_Name))
                p_rel.append(str.upper(s.Relation))
                p_rel_name.append(str.upper(s.Relation_Name))
                p_nd.append(s.NightDuty_Permitted)
                p_aadhaar3.append(s.Aadhaar_ID)
                p_mobile3.append(s.Mobile)
                p_address3.append(s.Address_Outside_PSN)
                p_remarks3.append(s.Remarks)
                p_dob3.append(s.Year_Of_Birth)
                if(s.Photo_File_Name):
                    p_photo3.append(str(s.Photo_File_Name))
                

                m_validity_original = datetime.datetime.strptime(str(s.Validity), '%Y-%m-%d')
                mval_formatted_date=m_validity_original.strftime("%d-%m-%Y")
                p_maid_validity.append(str(mval_formatted_date))
        
        your_list_as_json["Maid_id"]=p_maid_id
        your_list_as_json["Maid_Name"]=p_maid_name
        your_list_as_json["Rel"]=p_rel     
        your_list_as_json["Rel_Name"]=p_rel_name
        your_list_as_json["ND"]=p_nd
        your_list_as_json["Aadhaar3"]=p_aadhaar3
        your_list_as_json["Mobile3"]=p_mobile3       
        your_list_as_json["Address3"]=p_address3  
        your_list_as_json["Remarks3"]=p_remarks3
        your_list_as_json["Validity"]=p_maid_validity
        your_list_as_json["DOB3"]=p_dob3
        your_list_as_json["Photo_File_Name3"]=p_photo3
           
        return HttpResponse(json.dumps(your_list_as_json),content_type ="application/json")

    context={}


    return render(request,"searchRoom.html",
    context)


#login method
def login(request):
    #context={}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username =username , password=password)
        user_str=str(user)
        if user_str=='cg_sd':
            dj_login(request , user)
            #context["status"]="Successfully logged in."
            messages.success(request,"Successfully logged in.")
            return redirect('vehicle_transaction')
        elif user_str=='gg_sd':
            dj_login(request , user)
            #context["status"]="Successfully logged in."
            messages.success(request,"Successfully logged in.")
            return redirect('maid_transaction')
        elif user is not None:
            dj_login(request , user)
            #context["status"]="Successfully logged in."
            messages.success(request,"Successfully logged in.")
            return redirect('demography')
        else:
            #context["errorStatus"]="Invalid credentials. Please try again."
            messages.error(request,"Invalid credentials.")
            return redirect('home')
    return HttpResponse('404 - Not Found')
#logout Method                
def logout(request):
	if request.user.is_authenticated:
		deauth(request)
	return redirect('home')

# @login_required
# def maid(request):
#     context={}
#     maid_form=add_maid_form()

#     if request.method=="POST":
#         maid_form=add_maid_form(request.POST,request.FILES)
#         if maid_form.is_valid():
#             data=maid_form.save()
#             #data=form.save(commit=FALSE)
#             #data.save()
#             context["status"]="{} Added Successfully. In case there are more maids, please fill the form again".format(data.Maid_Name)
#         else:
#             context["errorStatus"]="Please correct the mistakes and re-submit"
#             #return render(request, "demography.html", {'form':form})

#     context["maid_form"] =maid_form

#     return render(request,"maid.html",
#     context)

@login_required
@user_passes_test(is_staff)
def emergency(request):
    context={}
    emergency_form=add_emergency_form()

    if request.method=="POST":
        emergency_form=add_emergency_form(request.POST,request.FILES)
        if emergency_form.is_valid():
            data=emergency_form.save()
            #data=form.save(commit=FALSE)
            #data.save()
            context["status"]="{} Added Successfully. In case there are more emergency contacts, please fill the form again".format(data.Emergency_Contact_Name)
        else:
            context["errorStatus"]="Please correct the mistakes and re-submit"
            #return render(request, "demography.html", {'form':form})

    context["emergency_form"] =emergency_form

    return render(request,"emergency.html",
    context)

@login_required
@user_passes_test(is_staff)
def maintenance(request):
    context={}
    maintenance_form=add_maintenance_form()

    if request.method=="POST":
        maintenance_form=add_maintenance_form(request.POST,request.FILES)
        if maintenance_form.is_valid():
            data=maintenance_form.save()
            #data=form.save(commit=FALSE)
            #data.save()
            context["status"]="Details added Successfully"
        else:
            context["errorStatus"]="Please correct the mistakes and re-submit"
            #return render(request, "demography.html", {'form':form})

    context["maintenance_form"] =maintenance_form

    return render(request,"maintenance.html",
    context)

@login_required
def vehicle_transaction(request):
    sticker_num=request.GET.get('Sticker_Number')
    if sticker_num is not None:
        sticker_num=int(sticker_num)

    sat=Vehicle.objects.filter(Existing_Sticker_Number=sticker_num, Status='Y')
    v_num=[]
    v_owner=[]
    #v_mobile=[]
    v_validity=[]
    m_in_out=[]

    your_list_as_json={}

    max_transaction_date = (
        VehicleTransaction.objects.filter(Sticker_Number=sticker_num, Status='Y')
            .annotate(common=Value(1))
            .values('common')
            .annotate(max_trans=Max('Updated_Date'))
            .values('max_trans')
    )
    

    for date in max_transaction_date:
        max_trans_date=date['max_trans']


    in_out=''
    in_out_temp=VehicleTransaction.objects.filter(Updated_Date=max_trans_date,Sticker_Number=sticker_num, Status='Y')
    
    for n in in_out_temp:
        in_out=n.In_Out
    
    if(in_out=='In'):
        in_out='Out'
    elif(in_out=='Out'):
        in_out='In'

    if(max_trans_date is None):
        in_out='In'
    
    if sat:
        for s in sat:
            
            v_num.append(str.upper(s.Vehicle_No))
            original_date = datetime.strptime(str(s.Validity), '%Y-%m-%d')
            formatted_date = original_date.strftime("%d-%m-%Y")
            v_validity.append(formatted_date)
            m_in_out.append(in_out)
            
            if(s.Type_Of_Owner=='ashramResident'):               
                veh_dtls=Demography.objects.filter(id=s.Member_Name_id, Status='Y')
                
                for v in veh_dtls:
                    v_owner.append(str.upper(v.Name))
                    
                    #v_mobile.append(v.Mobile) enable after make migrations error is closed
                    # TODO validity after resolving make migrations error
            else:
                v_owner.append(str.upper(s.Owner_Name))
                #v_mobile.append(v.Mobile) enable after make migrations error is closed

    
    if sticker_num:
        if v_num != []:
            your_list_as_json['num'] = v_num
            your_list_as_json['name'] = v_owner
            #your_list_as_json['mobile'] = v_mobile
            your_list_as_json['validity'] = v_validity
            your_list_as_json['in_out'] = m_in_out
            return HttpResponse(json.dumps(your_list_as_json) ,content_type ="application/json")

    context={}
    vehicle_tr_form=vehicle_transaction_form()

    if request.method=="POST":
        vehicle_tr_form=vehicle_transaction_form(request.POST,request.FILES)
        if vehicle_tr_form.is_valid():
            data=vehicle_tr_form.save()
            context["status"]="Vehicle permitted."
        else:
            context["errorStatus"]="Please correct the mistakes and re-submit"

    context["vehicle_tr_form"] =vehicle_tr_form


    return render(request,"transaction_vehicle.html",
    context)

@login_required
def temp_vehicle_transaction(request):
    vehicle_no=request.GET.get('Vehicle_No')

    sat=TempVehicle.objects.filter(Vehicle_No=vehicle_no, Status='Y')
    
    v_num=[]
    v_name=[]
    v_ref_name=[]
    v_veh_type=[]
    v_date_in=[]
    v_date_out=[]
    m_in_out=[]
    

    max_transaction_date = (
        TempVehicleTransaction.objects.filter(Vehicle_No=vehicle_no, Status='Y')
            .annotate(common=Value(1))
            .values('common')
            .annotate(max_trans=Max('Updated_Date'))
            .values('max_trans')
    )
    

    for date in max_transaction_date:
        max_trans_date=date['max_trans']

    in_out=''
    in_out_temp=TempVehicleTransaction.objects.filter(Updated_Date=max_trans_date,Vehicle_No=vehicle_no, Status='Y')
    

    for n in in_out_temp:
        in_out=n.In_Out
        
    
    if(in_out=='In'):
        in_out='Out'
    elif(in_out=='Out'):
        in_out='In'

    if(max_trans_date is None):
        in_out='In'

    your_list_as_json={}
    
    if sat:
        for s in sat:
            
            v_num.append(str.upper(s.Vehicle_No))
            v_name.append(str.upper(s.Name))
            v_ref_name.append(str.upper(s.Reference_Person_in_Ashram))
            v_veh_type.append(str.upper(s.Type_Of_Vehicle))
            original_date_in = str(s.Date_in)
            #formatted_date_in = original_date_in.strftime("%d-%m-%Y")
            v_date_in.append(original_date_in)
            original_date_out = str(s.Date_out)
            #formatted_date_out = original_date_out.strftime("%d-%m-%Y")
            v_date_out.append(original_date_out)
            m_in_out.append(in_out)
    
            
            

    
    if vehicle_no:
        if v_num != []:
            your_list_as_json['num'] = v_num
            your_list_as_json['name'] = v_name
            your_list_as_json['v_ref_name'] = v_ref_name
            your_list_as_json['v_veh_type'] = v_veh_type
            #your_list_as_json['mobile'] = v_mobile
            your_list_as_json['date_in'] = v_date_in
            your_list_as_json['date_out'] = v_date_out
            your_list_as_json['in_out'] = m_in_out
            print(your_list_as_json)
            return HttpResponse(json.dumps(your_list_as_json) ,content_type ="application/json")

    context={}
    temp_vehicle_tr_form=temp_vehicle_transaction_form()

    if request.method=="POST":
        temp_vehicle_tr_form=temp_vehicle_transaction_form(request.POST,request.FILES)
        if temp_vehicle_tr_form.is_valid():
            data=temp_vehicle_tr_form.save()
            context["status"]="Vehicle permitted."
        else:
            context["errorStatus"]="Please correct the mistakes and re-submit"

    context["temp_vehicle_tr_form"] =temp_vehicle_tr_form


    return render(request,"transaction_temp_vehicle.html",
    context)


@login_required
@user_passes_test(is_staff)
def maid_new(request):
    context={}
    maid_new_form=add_maid_new_form()

    if request.method=="POST":
        Maid_ID=request.POST.get('Maid_ID')
        Maid_Name=request.POST.get('Maid_Name')
        Relation=request.POST.get('Relation')
        Relation_Name=request.POST.get('Relation_Name')
        NightDuty_Permitted=request.POST.get('NightDuty_Permitted')
        Year_Of_Birth=request.POST.get('Year_Of_Birth')
        Aadhaar_ID=request.POST.get('Aadhaar_ID')
        Mobile=request.POST.get('Mobile')
        Address_Outside_PSN=request.POST.get('Address_Outside_PSN')
        Remarks=request.POST.get('Remarks')
        Room=request.POST.getlist('Room')
        Photo_File_Name=request.POST.get('Photo_File_Name')

        if not Maid_ID:
            print('here in something')
            max_token_no = (
            Maid.objects
           .annotate(common=Value(1))
           .values('common')
           .annotate(max_token_num=Max('Maid_ID'))
           .values('max_token_num')
            )
        

            for n in max_token_no:
                max_token_no=n['max_token_num']

            Maid_ID=max_token_no+1
        
        maid_details=Maid(
            Maid_ID=Maid_ID,
            Maid_Name=Maid_Name,
            Relation=Relation,
            Relation_Name=Relation_Name,
            NightDuty_Permitted=NightDuty_Permitted,
            Year_Of_Birth=Year_Of_Birth,
            Aadhaar_ID=Aadhaar_ID,
            Mobile=Mobile,
            Address_Outside_PSN=Address_Outside_PSN,
            Remarks=Remarks,
            Photo_File_Name=Photo_File_Name
            )
        
        maid_details.save()
        maid_details.Room.add(*Room)
        context["status"]="Maid with Token No. {} added Successfully.".format(Maid_ID) 

    context["maid_new_form"] =maid_new_form

    return render(request,"maid_new.html",
    context)

@login_required
def maid_transaction(request):
    maidID=request.GET.get('Maid_ID')
    # if maidID is not None:
    #     maidID=int(maidID)

    sat=Maid.objects.filter(Maid_ID=maidID, Status='Y')

    max_valid_date = (
    maid_renewal.objects
           .filter(Maid_ID=maidID)
           .annotate(common=Value(1))
           .values('common')
           .annotate(max_validity=Max('Validity'))
           .values('max_validity')
)

    for date in max_valid_date:
        max_validity_date=date['max_validity']

    if(max_validity_date is None):
        max_validity_date='2021-09-30'


    max_transaction_date = (
        MaidTransaction.objects.filter(Maid_ID=maidID, Status='Y')
            .annotate(common=Value(1))
            .values('common')
            .annotate(max_trans=Max('Updated_Date'))
            .values('max_trans')
    )
    

    for date in max_transaction_date:
        max_trans_date=date['max_trans']

    in_out=''
    in_out_temp=MaidTransaction.objects.filter(Updated_Date=max_trans_date,Maid_ID=maidID, Status='Y')
    

    for n in in_out_temp:
        in_out=n.In_Out
        print(in_out)
    
    if(in_out=='In'):
        in_out='Out'
    elif(in_out=='Out'):
        in_out='In'

    if(max_trans_date is None):
        in_out='In'
    

    m_name=[]
    #m_mobile=[]
    m_night_duty=[]
    m_photo=[]
    m_validity=[]
    m_room=[]
    m_in_out=[]
    
    

    your_list_as_json={}
    if sat:
        for s in sat:            
            m_name.append(str.upper(s.Maid_Name))
            #m_mobile.append(s.Mobile)
            m_night_duty.append(str.upper(s.NightDuty_Permitted))
            m_photo.append(str(s.Photo_File_Name))
            original_date = datetime.strptime(str(max_validity_date), '%Y-%m-%d')
            formatted_date = original_date.strftime("%d-%m-%Y")    
            m_validity.append(formatted_date)
            m_in_out.append(in_out)

            room_details=s.Room.all()
            for r in room_details:
                m_room.append(str.upper(r.Room))
            
    
    if maidID:
        if m_name != []:
            your_list_as_json['name'] = m_name
            #your_list_as_json['mobile'] = m_mobile
            your_list_as_json['night_duty'] = m_night_duty
            your_list_as_json['photo'] = m_photo
            your_list_as_json['room']=m_room
            your_list_as_json['validity'] = m_validity
            your_list_as_json['in_out'] = m_in_out
            
            return HttpResponse(json.dumps(your_list_as_json),content_type ="application/json")

    context={}

    maid_tr_form=maid_transaction_form()
    
    

    if request.method=="POST":
        maid_tr_form=maid_transaction_form(request.POST,request.FILES)
        
        if maid_tr_form.is_valid():
            maid_tr_form.fields["In_Out"].value = in_out
            data=maid_tr_form.save()
            context["status"]="Maid permitted."
        else:
            context["errorStatus"]="Please correct the mistakes and re-submit"

    context["maid_tr_form"] =maid_tr_form
    
    return render(request,"transaction_maid.html",
    context)



@login_required
def maidRenewal(request):
    print('in renewal')
    maidID=request.GET.get('Maid_ID')
    # if maidID is not None:
    #     maidID=int(maidID)

    sat=Maid.objects.filter(Maid_ID=maidID, Status='Y')

    max_valid_date = (
            maid_renewal.objects
           .filter(Maid_ID=maidID)
           .annotate(common=Value(1))
           .values('common')
           .annotate(max_validity=Max('Validity'))
           .values('max_validity')
)

    for date in max_valid_date:
        max_validity_date=date['max_validity']

    if(max_validity_date is None):
        print('none')
        max_validity_date='2021-09-30'

    m_validity_remarks=''

    year=datetime.now().year
    month=datetime.now().month
    day=datetime.now().day
    
    date_of_last_day_of_quarter=datetime(2021,1,1)
    
    if(month==3 or month==6 or month==9 or month==12):    
        if(day>=15):
            if(month==12):
                quarter=month//3
                last_month_of_quarter=3
                date_of_last_day_of_quarter = datetime(year+1, last_month_of_quarter, monthrange(year, last_month_of_quarter)[1])
            else:
                quarter=month//3 +1
                last_month_of_quarter = 3 * quarter
                date_of_last_day_of_quarter = datetime(year, last_month_of_quarter, monthrange(year, last_month_of_quarter)[1])
            
        else:
            quarter=month//3
            last_month_of_quarter = 3 * quarter
            date_of_last_day_of_quarter = datetime(year, last_month_of_quarter, monthrange(year, last_month_of_quarter)[1])

    else:
        quarter=month//3 +1
        last_month_of_quarter = 3 * quarter 
        date_of_last_day_of_quarter = datetime(year, last_month_of_quarter, monthrange(year, last_month_of_quarter)[1])

    validity=str(date_of_last_day_of_quarter.date())


    if(validity==str(max_validity_date)):
        m_validity_remarks='Renewal is already done. Next renewal window will be opened shortly.'

    m_name=[]
    m_mobile=[]
    m_night_duty=[]
    m_photo=[]
    m_validity=[]
    m_room=[]
    m_aadhaar=[]
    

    your_list_as_json={}
    if sat:
        for s in sat:            
            m_name.append(str.upper(s.Maid_Name))
            m_mobile.append(s.Mobile)
            m_night_duty.append(str.upper(s.NightDuty_Permitted))
            m_photo.append(str(s.Photo_File_Name))
            m_aadhaar.append(s.Aadhaar_ID)
            original_date = datetime.strptime(str(max_validity_date), '%Y-%m-%d')
            formatted_date = original_date.strftime("%d-%m-%Y")    
            m_validity.append(formatted_date)


            room_details=s.Room.all()
            for r in room_details:
                m_room.append(str.upper(r.Room))

    if maidID:
        if m_name != []:
            your_list_as_json['name'] = m_name
            your_list_as_json['mobile'] = m_mobile
            your_list_as_json['night_duty'] = m_night_duty
            your_list_as_json['photo'] = m_photo
            your_list_as_json['validity'] = m_validity
            your_list_as_json['room']=m_room
            your_list_as_json['aadhaar']=m_aadhaar
            your_list_as_json['validity_remarks']=m_validity_remarks
    
           
            return HttpResponse(json.dumps(your_list_as_json),content_type ="application/json")

    context={}

    maid_ren_form=maid_renewal_form()

    if request.method=="POST":
        maid_ren_form=maid_renewal_form(request.POST,request.FILES)
        if maid_ren_form.is_valid():
            #maid_ren_form.Validity='2021-03-31'
            data=maid_ren_form.save()
            context["status"]="Validity is renewed"
        else:
            context["errorStatus"]="Please correct the mistakes and re-submit"

    context["maid_ren_form"] =maid_ren_form


    return render(request,"maidRenewal.html",
    context)


@login_required
@user_passes_test(is_staff)
def temp_vehicle(request):    
    context={}
    temp_veh_form=temp_vehicle_form()
    
    if request.method=="POST":
        temp_veh_form=temp_vehicle_form(request.POST,request.FILES)
        if temp_veh_form.is_valid():
            data=temp_veh_form.save()
            #data=form.save(commit=FALSE)
            #data.save()
            context["status"]="{} Added Successfully. ".format(data.Vehicle_No)
        else:
            context["errorStatus"]="Please correct the mistakes and re-submit"
            #return render(request, "demography.html", {'form':form})

    context["temp_veh_form"] =temp_veh_form

    return render(request,"temp_vehicle.html",
    context)


@login_required
def vehicleRenewal(request):
    sticker_num=request.GET.get('Sticker_Num')
    print(sticker_num)
    # if maidID is not None:
    #     maidID=int(maidID)

    sat=Vehicle.objects.filter(Existing_Sticker_Number=sticker_num, Status='Y')
    print(sat)
    max_valid_date = (
            vehicle_renewal.objects
           .filter(Sticker_Num=sticker_num)
           .annotate(common=Value(1))
           .values('common')
           .annotate(max_validity=Max('Validity'))
           .values('max_validity')
)

    for date in max_valid_date:
        max_validity_date=date['max_validity']

    print(max_validity_date)

    if(max_validity_date is None):
        max_validity_date='2021-12-31'

    print(max_validity_date)

    

    m_validity_remarks=''

    year=datetime.now().year
    month=datetime.now().month
    
    date_of_last_day_of_year=datetime(2021,1,1)
    
    if(month==12):    
        date_of_last_day_of_year = datetime(year+1, 12, 31)
            
    else:
        date_of_last_day_of_year = datetime(year, 12, 31)

    validity=str(date_of_last_day_of_year.date())

    if(validity==str(max_validity_date)):
        m_validity_remarks='Renewal is already done. Next renewal window will be opened shortly.'

    v_num=[]
    v_owner=[]
    #v_mobile=[]
    v_validity=[]
    
    your_list_as_json={}   

    
    if sat:
        for s in sat:
            print(s.Vehicle_No)            
            v_num.append(str.upper(s.Vehicle_No))
            # original_date = datetime.strptime(str(s.Validity), '%Y-%m-%d')
            # formatted_date = original_date.strftime("%d-%m-%Y")
            v_validity.append(validity)
            
            if(s.Type_Of_Owner=='ashramResident'):               
                veh_dtls=Demography.objects.filter(id=s.Member_Name_id, Status='Y')
                
                for v in veh_dtls:
                    v_owner.append(str.upper(v.Name))
                    
                    #v_mobile.append(v.Mobile) enable after make migrations error is closed
                    # TODO validity after resolving make migrations error
            else:
                v_owner.append(str.upper(s.Owner_Name))
                #v_mobile.append(v.Mobile) enable after make migrations error is closed

    print('here/there')
    print(v_num)
    
    if sticker_num:
        if v_num != []:
            your_list_as_json['num'] = v_num
            your_list_as_json['name'] = v_owner
            #your_list_as_json['mobile'] = v_mobile
            your_list_as_json['validity'] = v_validity
            your_list_as_json['validity_remarks'] = m_validity_remarks
            return HttpResponse(json.dumps(your_list_as_json) ,content_type ="application/json")

    context={}
    

    veh_ren_form=vehicle_renewal_form()

    if request.method=="POST":
        veh_ren_form=vehicle_renewal_form(request.POST,request.FILES)
        if veh_ren_form.is_valid():
            #maid_ren_form.Validity='2021-03-31'
            data=veh_ren_form.save()
            context["status"]="Validity is renewed"
        else:
            context["errorStatus"]="Please correct the mistakes and re-submit"

    context["veh_ren_form"] =veh_ren_form


    return render(request,"vehicleRenewal.html",
    context)



    