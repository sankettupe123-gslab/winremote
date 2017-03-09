
from django.conf.urls import url, include
from . import views

urlpatterns = [
url(r'^usercmd/',views.remote_cmd, name='remote_cmd' ),
url(r'^$', views.index, name='index'),
url(r'^remotecmd/', views.cmd_input, name='cmd_input'),
url(r'^history/',views.history_cmd, name='history_cmd'),
url(r'^tool/',views.tools_input, name='tools_input'),
url(r'^tools/',views.tools_output, name='tools_output'),
url(r'^login/',views.start_login, name='start_login'),
url(r'^check/',views.check_login, name='check_login'),
url(r'^startapp/',views.startapp_input, name='startapp_input'),
url(r'^runapp/',views.startapp_output, name='startapp_output'),
]


