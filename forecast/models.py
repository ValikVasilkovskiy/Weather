from django.db import models
from datetime import datetime

class DayWeatherForecast(models.Model):
    date = models.DateField(null=False)
    forecast_day_temp = models.IntegerField(null=False)
    forecast_night_temp = models.IntegerField(null=False)

    def average_temp_per_day(self):
        return (self.forecast_day_temp + self.forecast_night_temp) / 2



