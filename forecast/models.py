from django.db import models


class DayWeatherForecast(models.Model):
    name = models.CharField(max_length=100, default="Sunday")
    date = models.DateField(null=False)
    forecast_day_temp = models.IntegerField(null=False)
    forecast_night_temp = models.IntegerField(null=False)

    def average_temp_per_day(self):
        return (self.forecast_day_temp + self.forecast_night_temp) / 2

    def __str__(self):
        return (self.name)
