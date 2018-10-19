from django.shortcuts import render

# Create your views here.

def weather_list(request):
    return render(request, 'forecast/weather_list.html', {})
