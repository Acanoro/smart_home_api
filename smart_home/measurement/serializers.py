from rest_framework import serializers

from measurement.models import SensorModel, MeasurementModel


class MeasurementSerializer(serializers.ModelSerializer):
    related_sensor = serializers.PrimaryKeyRelatedField(queryset=SensorModel.objects.all())

    class Meta:
        model = MeasurementModel
        fields = ['id', 'related_sensor', 'temperature', 'created_at', 'img']


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorModel
        fields = ['id', 'name', 'description']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = SensorModel
        fields = ['id', 'name', 'description', 'measurements']
