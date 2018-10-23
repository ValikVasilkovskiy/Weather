from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.weather_list, name='weather_list')
]
