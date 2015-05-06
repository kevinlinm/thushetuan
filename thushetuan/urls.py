from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'thushetuan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^appointment/', include('appointment.urls')),
    url(r'^draw/', include('draw.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
