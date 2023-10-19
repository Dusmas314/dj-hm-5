from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)


class Measurement(models.Model):
    ID = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

