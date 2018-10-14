from django.conf.urls import url

from . import views

#from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.logout_page, name="log out"),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^home/$', views.index, name='index'),
    url(r'^getnextnumber/$', views.get_next_number),
    url(r'^getnumberstatus/$', views.get_number_status),
    url(r'^reports/$', views.reports),
    url(r'^mangaereport/$', views.mangae_report),
    url(r'^managereservation/$', views.manage_reservation),
    url(r'^managerule/$', views.manage_rule),
    #url(r'^home/$', views.index),
    #url(r'^home/$', views.index),
    #url(r'^home/$', views.index),
]