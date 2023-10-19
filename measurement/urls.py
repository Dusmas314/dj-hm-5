from django.urls import path
from .views import Sensors, Measurements, UpdateSensor, SensorDetail

urlpatterns = [
    path('sensors/', Sensors.as_view()),
    path('sensors/<int:pk>/', UpdateSensor.as_view()),
    path('measurements/<sensor>/', Measurements.as_view()),
    path('sensor/<int:pk>/', SensorDetail.as_view())
]