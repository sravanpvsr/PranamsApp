from django.conf.urls import url
from PranamsApp import views
from django.views.static import serve 

from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView

urlpatterns=[
    url(r'^institution/$',views.institutionApi),
    url(r'^$',TemplateView.as_view(template_name='home.html'),name='home'),
    #url(r'^home/$',views.home , name='home'),
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
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)