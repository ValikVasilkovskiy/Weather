from django.shortcuts import render, get_object_or_404
from .models import DayWeatherForecast

import calendar
from datetime import datetime

# Create your views here.

def weather_list(request):
    forecasts = DayWeatherForecast.objects.all()
    return render(request, 'forecast/weather_list.html', {
        "forecasts": forecasts,})

def day_detail(request, pk):
    day = get_object_or_404(DayWeatherForecast, pk=pk)
    return render(request, 'forecast/day_detail.html', {'day': day})
