from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as authViews


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/login/$', authViews.login, name='login')
]
