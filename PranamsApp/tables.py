# tutorial/tables.py
import django_tables2 as tables
from .models import *

class VehicleTable(tables.Table):
    class Meta:
        model = Vehicle
        template_name = "django_tables2/bootstrap.html"
        fields = ("Vehicle_No", )


# class VehicleFilter(django_filters.FilterSet):
#     #start_date=DateFilter(field_name="RC_Valid_Upto",lookup_expr='gte')
#     Vehicle_No=CharFilter(field_name='Vehicle_No', lookup_expr='icontains')
#     #Room=CharFilter(field_name='Room', lookup_expr='icontains')

#     class Meta:
#         model=Vehicle
#         fields=['Vehicle_No','Existing_Sticker_Number','Mobile','Room']