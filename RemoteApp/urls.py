from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = {
    url(r'^winremote/',include('WinRemote.urls'))
}

