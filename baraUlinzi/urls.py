"""baraUlinzi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from log import views
from log.forms import LoginForm



urlpatterns = [
    url(r'^ussd/',include('ussd.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$',auth_views.login,{'template_name':'login.html','authentication_form':LoginForm},name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^home/$', views.home, name='home'),
    url(r'^sacco/$', views.sacco, name='sacco'),
    url(r'^driverProfile/$', views.driverProfile, name='driverProfile'),
    url(r'^sacco/delete/(?P<pk>\d+)/$',views.delete_sacco, name='delete_sacco'),
    url(r'^home/vehicle/(?P<vehiclereg>\w+)/$',views.vehicle_details, name='vehicle_details'),
    url(r'^driverProfile/$',views.driver_details, name='driver_details'),
    url(r'^driverProfile/(?P<vehiclereg>\w+)/$',views.driver_details, name='driver_details'),
    url(r'^home/sacco_details/(?P<pk>\d+)/$',views.sacco_details, name='sacco_details'),
    url(r'^drivers/$', views.drivers, name='drivers'),
    url(r'^drivers/delete/(?P<pk>\d+)/$', views.delete_driver, name='delete_driver'),
    url(r'^profile/$', views.update_profile, name='profile'),
    url(r'',include('log.urls')),
   
]
