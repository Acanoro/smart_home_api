from rest_framework import generics
from measurement.models import SensorModel, MeasurementModel
from measurement.serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


class SensorListCreateView(generics.ListCreateAPIView):
    queryset = SensorModel.objects.all()
    serializer_class = SensorSerializer


class SensorRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = SensorModel.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreateView(generics.CreateAPIView):
    queryset = MeasurementModel.objects.all()
    serializer_class = MeasurementSerializer
