from django.conf import settings
from django.conf.urls.static import static
#the above 2 imports help to serve media files
from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('properties/<int:id>/',property_grid,name='property_grid'),
    path('agent registration/',agent_reg,name='agent_reg'),
    path('agent login/',agent_login,name='agent_login'),
    path('forgot password/',forgot_pwd,name='forgot_pwd'),
    path('agent dashboard/',agent_dash,name='agent_dash'),
    path('agent dashboard/edit profile/',edit_profile,name='edit_profile'),
    path('agent logout/',agent_logout,name='agent_logout'),
    path('agent dashboard/add property/',add_property,name='add_property'),
    path('propertydetails/<int:id>/',single_property,name='single_property'),
    path('editlodge/<int:id>/',editlodge,name='editlodge'),
    path('deletelodge/<int:id>/',deletelodge,name='deletelodge'),
    path('home/selectschool/',selectschool,name='selectschool'),
    path('home/selectschool/',selectschool,name='selectschool'),
    path('home/selectschool/roomates/<str:name>/',roomates_grid,name='roomates_grid'),
    path('schools/roomates/',roomates_grid,name='roomates_grid'),
    path('roomates/fillform/<str:name>',roomy_form,name='roomy_form'),  
    path('passwordreset/<str:email>/',pwd_reset,name='pwd_reset'),
    path('reset mail sent/',resetmail_sent,name='resetmail_sent')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

