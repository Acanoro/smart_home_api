from django.core.validators import MinValueValidator
from django.db import models


class SensorModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=1000, verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'


class MeasurementModel(models.Model):
    related_sensor = models.ForeignKey(
        SensorModel,
        on_delete=models.CASCADE,
        verbose_name='Датчик',
        related_name='measurements'
    )
    temperature = models.DecimalField(
        default=0,
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name='Температура при измерении'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время измерения')
    img = models.ImageField(verbose_name='Изображение', blank=True, null=True)

    def __str__(self):
        return f'MeasurementObject'

    class Meta:
        verbose_name = 'Измерение температуры'
        verbose_name_plural = 'Измерения температуры'
