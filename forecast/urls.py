from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.weather_list, name='weather_list'),
    url(r'^day/(?P<pk>\d+)/$', views.day_detail, name='day_detail'),
]
