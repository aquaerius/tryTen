from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.service_list, name='service_list'),
    url(r'^owners/$', views.owners_detail, name='owners_detail'),
    url(r'^contractors/$', views.contractors_detail, name='contractors_detail'),
]
