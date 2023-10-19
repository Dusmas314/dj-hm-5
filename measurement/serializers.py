from rest_framework import serializers
from .models import Sensor, Measurement

# TODO: опишите необходимые сериализаторы


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['ID', 'temperature', 'time']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


class MeasurementSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature']

