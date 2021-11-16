import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class VehicleFilter(django_filters.FilterSet):
    #start_date=DateFilter(field_name="RC_Valid_Upto",lookup_expr='gte')
    Vehicle_No=CharFilter(field_name='Vehicle_No', lookup_expr='icontains')
    #Room=CharFilter(field_name='Room', lookup_expr='icontains')

    class Meta:
        model=Vehicle
        fields=['Vehicle_No','Existing_Sticker_Number','Mobile','Room']


# class MaidFilter(django_filters.FilterSet):
#     #start_date=DateFilter(field_name="RC_Valid_Upto",lookup_expr='gte')
#     Maid_Name=CharFilter(field_name='Maid_Name', lookup_expr='icontains')
    
#     class Meta:
#         model=Maid
#         fields=['Maid_ID','Maid_Name','NightDuty_Permitted','Room__Room']

class MaidRenewalFilter(django_filters.FilterSet):    
    #Name = CharFilter(field_name='Maid__Maid_ID', lookup_expr='icontains')
    #, label='', widget=TextInput(attrs={'placeholder': 'Set Code', 'class': 'page-input', 'style': 'width: 150px;'}))
    #Name=CharFilter(field_name='Name', lookup_expr='icontains')
    class Meta:
        model=maid_renewal
        fields=['Maid_ID','Validity']


class RoomFilter(django_filters.FilterSet):
    #start_date=DateFilter(field_name="RC_Valid_Upto",lookup_expr='gte')
    Name=CharFilter(field_name='Name', lookup_expr='icontains')
    #Room=CharFilter(field_name='Room', lookup_expr='icontains')

    class Meta:
        model=Demography
        fields=['Room','Name']


class TempVehicleFilter(django_filters.FilterSet):
    #start_date=DateFilter(field_name="RC_Valid_Upto",lookup_expr='gte')
    Vehicle_No=CharFilter(field_name='Vehicle_No', lookup_expr='icontains')
    Name=CharFilter(field_name='Name', lookup_expr='icontains')
    Reference_Person_in_Ashram=CharFilter(field_name='Reference_Person_in_Ashram', lookup_expr='icontains')
    #Room=CharFilter(field_name='Room', lookup_expr='icontains')

    class Meta:
        fields=['Date_in','Date_out']

        