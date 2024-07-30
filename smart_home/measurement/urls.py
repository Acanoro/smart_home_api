from django.urls import path
from measurement.views import SensorListCreateView, SensorRetrieveUpdateView, MeasurementCreateView

urlpatterns = [
    path('sensor/', SensorListCreateView.as_view(), name='sensor-list-create'),
    path('sensor/<int:pk>/', SensorRetrieveUpdateView.as_view(), name='sensor-retrieve-update'),
    path('measurement/', MeasurementCreateView.as_view(), name='measurement-create'),
]
