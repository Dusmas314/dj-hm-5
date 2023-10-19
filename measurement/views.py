# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import generics
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSensorSerializer
from .models import Sensor, Measurement


class Sensors(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class UpdateSensor(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class Measurements(generics.ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSensorSerializer


class SensorDetail(generics.ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

