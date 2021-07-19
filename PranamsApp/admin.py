from django.contrib import admin
from .models import add_demography,add_vehicle,add_maid,add_emergency,add_maintenance

admin.site.site_header="PRANAMS Administration"
# Register your models here.
admin.site.register(add_demography)
admin.site.register(add_maid)
admin.site.register(add_emergency)
admin.site.register(add_maintenance)
admin.site.register(add_vehicle)