from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages


from PranamsApp.models import Member_Category_Master,Institution_Master,Sub_Division_Master,Institution_Sub_Division_Map,Room_Type_Master,Room_Master,Gate_Master,add_demography, add_vehicle,add_maid,add_emergency,add_maintenance,vehicle_transaction
from PranamsApp.serializers import Member_Category_Master_Serializer,Institution_Master_Serializer,Sub_Division_Master_Serializer,Institution_Sub_Division_Map_Serializer,Room_Type_Master_Serializer,Room_Master_Serializer,Gate_Master_Serializer
from PranamsApp.forms import add_demography_form, add_occupant_form, add_vehicle_form,add_maid_form, add_emergency_form,add_maintenance_form,vehicle_transaction_form
from django.contrib.auth import authenticate,logout as deauth, login  as dj_login
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required

# Create your views here.   

@csrf_exempt

def institutionApi(request):
    
    if request.method=='GET':
        institution = Institution_Master.objects.all()
        institution_serializer = Institution_Master_Serializer(institution, many=True)
        return JsonResponse(institution_serializer.data, safe=False)

    elif request.method=='POST':
        institution_data=JSONParser().parse(request)
        institution_serializer = Institution_Master_Serializer(data=institution_data)
        if institution_serializer.is_valid():
            institution_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)

    elif request.method=='PUT':
        institution_data = JSONParser().parse(request)
        institution=Institution_Master.objects.get(Institution_ID=institution_data['Institution_ID'])
        institution_serializer=Institution_Master_Serializer(institution,data=institution_data)
        if institution_serializer.is_valid():
            institution_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)


@csrf_exempt
def SaveFile(request):
    file=request.FILES['uploadedFile']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name, safe=False)

# For HTML
def home(request):
    return render(request,"home.html")


@login_required
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
    
# def vehicle(request):
#     context={}
#     vehicle_form=add_vehicle_form()

#     # if request.method=='GET':
#     #     institution = Institution_Master.objects.all()
#     #     institution_serializer = Institution_Master_Serializer(institution, many=True)
#     #     return JsonResponse(institution_serializer.data, safe=False)

#     if request.method=="POST":
#         vehicle_form=add_vehicle_form(request.POST,request.FILES)
#         if vehicle_form.is_valid():
            
#             data=vehicle_form.save()
#             #data=form.save(commit=FALSE)
#             #data.save()
#             context["status"]="{} Added Successfully. In case there are more vehicles, please fill the form again".format(data.Vehicle_No)
#         else:
#             context["errorStatus"]="Please correct the mistakes and re-submit"
#             #return render(request, "demography.html", {'form':form})

#     context["vehicle_form"] =vehicle_form

#     return render(request,"vehicle.html",
#     context)

#Updated - 8-Jul-2021
@login_required
def vehicle(request):
    room_id=request.GET.get('Room')
    Member_Occupant=request.GET.get('Member_Occupant')

    sat=add_demography.objects.filter(Room=room_id, Status='Y')
    m_names=[]
    o_names=[]
    if sat:
        for s in sat:
            if Member_Occupant == 'member':
                if not s.Member_Occupant:
                    m_names.append(s.Name)
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
            return HttpResponse(your_list_as_json ,content_type ="application/json")
        else:

            your_list_as_json = json.dumps(o_names)
            
            return HttpResponse(your_list_as_json ,content_type ="application/json")                

    context={}
    vehicle_form=add_vehicle_form()                  
    #print(obj,sat)
    # if request.method=='GET':
    #     institution = Institution_Master.objects.all()
    #     institution_serializer = Institution_Master_Serializer(institution, many=True)
    #     return JsonResponse(institution_serializer.data, safe=False)
    
    if request.method=="POST":
        Room=request.POST.get('Room')
        Roominstance=Room_Master.objects.get(Room=Room)


        Vehicle_Available=request.POST.get('Vehicle_Available')
        Member_Occupant=request.POST.get('Member_Occupant')

        Member_Name=request.POST.get('Member_Name')
        memberinstance=add_demography.objects.get(Name=Member_Name)

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

        # print(Room,Vehicle_Available,Member_Occupant,Member_Name,DL_No,DL_Validity,Two_Four_Wheeler,
        #     Vehicle_No,RC_Valid_Upto,Insurance_Valid_Upto,Remarks,Gate_Name)            
        vehicle_details=add_vehicle(
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
                Existing_Sticker_Number=Existing_Sticker_Number

            )

        
        vehicle_details.save()
        vehicle_details.Gate_Name.add(*Gate_Name)
        context["status"]="Details added Successfully. In case there are more occupants, please fill the form again"
                 


    context["vehicle_form"] =vehicle_form
    


    return render(request,"vehicle.html",
    context)

def search(request):
    primaryMemberDisplay=add_demography.objects.all()
    #occupantDisplay=Room_Master.objects.all()
    #vehicleDisplay=add_vehicle
    return render(request,"search.html",
    {"add_demography":primaryMemberDisplay,
    #"Room_Master":occupantDisplay
    })

#login method
def login(request):
    #context={}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username =username , password=password)
        if user is not None:
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

@login_required
def maid(request):
    context={}
    maid_form=add_maid_form()

    if request.method=="POST":
        maid_form=add_maid_form(request.POST,request.FILES)
        if maid_form.is_valid():
            data=maid_form.save()
            #data=form.save(commit=FALSE)
            #data.save()
            context["status"]="{} Added Successfully. In case there are more maids, please fill the form again".format(data.Maid_Name)
        else:
            context["errorStatus"]="Please correct the mistakes and re-submit"
            #return render(request, "demography.html", {'form':form})

    context["maid_form"] =maid_form

    return render(request,"maid.html",
    context)

@login_required
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
# def add_demography_view(request):
#     return render(request,"")


# if request.GET.get('featured'):
#         featured_filter = request.GET.get('featured')
#         listings = Listing.objects.filter(featured_choices=featured_filter)
# else:
#         listings = Listing.objects.all()

@login_required
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
    context={}
    vehicle_tr_form=vehicle_transaction_form()

    if request.method=="POST":
        vehicle_tr_form=vehicle_transaction_form(request.POST,request.FILES)
        if vehicle_tr_form.is_valid():
            data=vehicle_tr_form.save()
            #data=form.save(commit=FALSE)
            #data.save()
            context["status"]="Vehicle permitted."
        else:
            context["errorStatus"]="Please correct the mistakes and re-submit"
            #return render(request, "demography.html", {'form':form})

    context["vehicle_tr_form"] =vehicle_tr_form

    return render(request,"transaction_vehicle.html",
    context)