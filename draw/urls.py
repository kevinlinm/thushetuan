from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^luck/$', views.luck),
    url(r'^(?P<draw_id>[0-9]+)/$', views.result),
]
