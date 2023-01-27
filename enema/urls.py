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
    path('home/selectschool/typeofroomy/<str:name>/',typeofroomy,name='typeofroomy'),
    path('home/selectschool/roomates/<str:name>/',roomates_grid,name='roomates_grid'),
    path('schools/roomates/',roomates_grid,name='roomates_grid'),
    path('roomates/fillform/<str:name>',roomy_form,name='roomy_form'),  
    path('passwordreset/<str:email>/',pwd_reset,name='pwd_reset'),
    path('reset mail sent/',resetmail_sent,name='resetmail_sent'),
    path('pay/<int:id>/',pay,name='pay'),
    path('roommatesingle/<int:id>/',roomate_single,name='roomate_single'),
    path('lodgepay/<int:id>/',lodge_pay,name='lodge_pay'),
    path('congratulations/',congrats,name='congrats'),
    path('admin_login/',admin_login,name='admin_login'),
    path('admindash/',admindash,name='admindash'),
    path('adminagentpanel/',admin_agentpanel,name='admin_agentpanel'),
    path('verify_agent/<int:id>/',verify_agent,name='verify_agent'),
    path('adminlodgepanel/',admin_lodgepanel,name='admin_lodgepanel'),
    path('toggle_lodgestatus/<int:id>/',toggle_lodgestatus,name='toggle_lodgestatus'),
    path('delete lodge/<int:id>/',admindelete_lodge,name='admindelete_lodge'),
    path('admin_showlodge/<int:id>/',admin_showlodge,name='admin_showlodge'),
    path('schedulodge_inspection/<int:id>/',schedulodge_inspection,name='schedulodge_inspection'),
    path('schedulehistory/<int:id>/',schedulehistory,name='schedulehistory'),
    path('reschedule_student/<int:id>/',reschedule_student,name='reschedule_student'),
    path('allschedulehistory/',allschedulehistory,name='allschedulehistory'),
    path('toggle_schedulehistory/<int:id>/',toggle_schedulehistory,name='toggle_schedulehistory'),
    path('admin_roomiespanel/',admin_roomiespanel,name='admin_roomiespanel'),
    path('admin_deleteroomy/<int:id>/',admin_deleteroomy,name='admin_deleteroomy'),
    path('admin_matchroomy/<int:id>/',admin_matchroomy,name='admin_matchroomy'),
    path('matchhistory/<int:id>/',matchhistory,name='matchhistory'),
    path('terms_of_service/',terms_of_service,name='terms_of_service'),
    path('privacypolicy/',privacypolicy,name='privacypolicy'),
    path('careers/',careers,name='careers')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

