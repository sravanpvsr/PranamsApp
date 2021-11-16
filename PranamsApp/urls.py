from django.conf.urls import url
from django.contrib import admin
from PranamsApp import views
from django.views.static import serve 

from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView

urlpatterns=[
    url(r'admin/$', admin.site.urls),
    url(r'^$',TemplateView.as_view(template_name='home.html'),name='home'),
    #url(r'^home/$',views.home , name='home'),
    url(r'^demography/$',views.demography,name="demography"),
    url(r'^occupant/$',views.occupant,name="occupant"),
    url(r'^vehicle/$',views.vehicle,name="vehicle"),
    url(r'^searchRoom/$',views.searchRoom,name="searchRoom"),
    url(r'^searchRoomCompact/$',views.searchRoomCompact,name="searchRoomCompact"),
    url(r'^searchVehicle/$',views.searchVehicle,name="searchVehicle"),
    #url(r'^searchMaid/$',views.searchMaid,name="searchMaid"),
    url(r'^login/$',views.login,name="login"),
    url(r'^logout/$',views.logout,name="logout"),
    #url(r'^maid/$',views.maid,name="maid"),
    url(r'^maid_new/$',views.maid_new,name="maid_new"),
    url(r'^emergency/$',views.emergency,name="emergency"),
    url(r'^maintenance/$',views.maintenance,name="maintenance"),
    url(r'^vehicle_transaction/$',views.vehicle_transaction,name="vehicle_transaction"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    url(r'^maid_transaction/$',views.maid_transaction,name="maid_transaction"),
    url(r'^maidRenewal/$',views.maidRenewal,name="maidRenewal"),
    url(r'^searchMaidRenewal/$',views.searchMaidRenewal,name="searchMaidRenewal"),
    url(r'^vehicleRenewal/$',views.vehicleRenewal,name="vehicleRenewal"),
    url(r'^temp_vehicle/$',views.temp_vehicle,name="temp_vehicle"),
    url(r'^searchTempVehicle/$',views.searchTempVehicle,name="searchTempVehicle"),
    url(r'^temp_vehicle_transaction/$',views.temp_vehicle_transaction,name="temp_vehicle_transaction"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)