from django import forms

from .models import DayWeatherForecast

class ForecastForm(forms.ModelForm):

    class Meta:
        model = DayWeatherForecast
        widgets = {
                    'date': forms.DateInput(attrs={'class':'date-input'}),
                    }
        fields = ('name', 'date', 'forecast_day_temp', 'forecast_night_temp',)

