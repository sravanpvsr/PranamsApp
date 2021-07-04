from django.conf.urls import url
from PranamsApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^institution/$',views.institutionApi),
    url(r'^home/$',views.home),
    url(r'^SaveFile$',views.SaveFile),
    url(r'^demography/$',views.demography,name="demography"),
    url(r'^occupant/$',views.occupant,name="occupant"),
    url(r'^vehicle/$',views.vehicle,name="vehicle"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)