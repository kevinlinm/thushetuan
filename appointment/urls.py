from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^nametag/$', views.nametag),
    url(r'^soccer/$', views.soccer),
    url(r'^book/$', views.book),
    url(r'^success/$', views.success),
]
