from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


from PranamsApp.models import Member_Category_Master,Institution_Master,Sub_Division_Master,Institution_Sub_Division_Map,Member_Master,Room_Type_Master,Room_Master,Occupant_Master,Gate_Master,Vehicle_Gate_Map,add_demography
from PranamsApp.serializers import Member_Category_Master_Serializer,Institution_Master_Serializer,Sub_Division_Master_Serializer,Institution_Sub_Division_Map_Serializer,Member_Master_Serializer,Room_Type_Master_Serializer,Room_Master_Serializer,Occupant_Master_Serializer,Gate_Master_Serializer,Vehicle_Gate_Map_Serializer
from PranamsApp.forms import add_demography_form, add_occupant_form, add_vehicle_form

from django.core.files.storage import default_storage

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
    
def vehicle(request):
    context={}
    vehicle_form=add_vehicle_form()

    # if request.method=='GET':
    #     institution = Institution_Master.objects.all()
    #     institution_serializer = Institution_Master_Serializer(institution, many=True)
    #     return JsonResponse(institution_serializer.data, safe=False)

    if request.method=="POST":
        vehicle_form=add_vehicle_form(request.POST,request.FILES)
        if vehicle_form.is_valid():
            
            data=vehicle_form.save()
            #data=form.save(commit=FALSE)
            #data.save()
            context["status"]="{} Added Successfully. In case there are more vehicles, please fill the form again".format(data.Vehicle_No)
        else:
            context["errorStatus"]="Please correct the mistakes and re-submit"
            #return render(request, "demography.html", {'form':form})

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
# def add_demography_view(request):
#     return render(request,"")


# if request.GET.get('featured'):
#         featured_filter = request.GET.get('featured')
#         listings = Listing.objects.filter(featured_choices=featured_filter)
# else:
#         listings = Listing.objects.all()
