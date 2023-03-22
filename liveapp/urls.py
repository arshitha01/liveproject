from django.urls import path
from liveapp import views

urlpatterns=[
             
            path('',views.index),
            path('about/',views.about),										
            path('services/',views.services),
            path('contact/',views.usercontact),
            path('admin_index/',views.admin_index),
            path('admin_login/',views.admin_login),
            path('admin_register/',views.admin_register),
            path('admin_logout/',views.admin_logout),
            path('ctable/',views.contactdisplay),
            path('sform/',views.sform),
            path('stable/',views.stable),
            path('stableupdate/',views.stableupdate),
            path('stabledelete/',views.stabledelete),
            path('gform/',views.gform),
            path('gtable/',views.gtable),
            path('gtableupdate/',views.gtableupdate),
            path('gtabledelete/',views.gtabledelete),
            path('getprice/',views.getprice),
            path('gettable/',views.gettable),


             ]