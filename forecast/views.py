from django.shortcuts import render
from .models import DayWeatherForecast

# Create your views here.

def weather_list(request):
    forecasts = DayWeatherForecast.objects.all()
    return render(request, 'forecast/weather_list.html', {"forecasts": forecasts})
