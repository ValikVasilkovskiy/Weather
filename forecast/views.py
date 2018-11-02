from django.shortcuts import render, get_object_or_404, redirect
from .models import DayWeatherForecast
from .forms import ForecastForm


def weather_list(request):
    forecasts = DayWeatherForecast.objects.all()
    return render(request, 'forecast/weather_list.html', {
        "forecasts": forecasts,})

def day_detail(request, pk):
    day = get_object_or_404(DayWeatherForecast, pk=pk)
    return render(request, 'forecast/day_detail.html', {'day': day})

def day_new(request):
    if request.method == "POST":
        form = ForecastForm(request.POST)
        forecast = form.save(commit=False)
        forecast.save()
        return redirect('day_detail', pk=forecast.pk)

    else:
        form = ForecastForm()
    return render(request, 'forecast/day_edit.html', {'form': form})


