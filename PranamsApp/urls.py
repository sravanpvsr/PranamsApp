from django.conf.urls import url
from PranamsApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^institution/$',views.institutionApi),
    url(r'^home/$',views.home , name='home'),
    url(r'^SaveFile$',views.SaveFile),
    url(r'^demography/$',views.demography,name="demography"),
    url(r'^occupant/$',views.occupant,name="occupant"),
    url(r'^vehicle/$',views.vehicle,name="vehicle"),
    url(r'^search/$',views.search,name="search"),
    url(r'^login/$',views.login,name="login"),
    url(r'^logout/$',views.logout,name="logout"),
    url(r'^maid/$',views.maid,name="maid"),
    url(r'^emergency/$',views.emergency,name="emergency"),
    url(r'^maintenance/$',views.maintenance,name="maintenance"),
    url(r'^vehicle_transaction/$',views.vehicle_transaction,name="vehicle_transaction"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)