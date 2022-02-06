from django.db import models
from django.contrib.auth.models import User

from tools.mixins import CreatedAndUpdatedAtMixin


class MeasureName(models.Model):
    name = models.CharField(max_length=128)
    generic = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User, related_name='body_parts', null=True, blank=True, default='', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Measure(CreatedAndUpdatedAtMixin, models.Model):        # basic one, without split into weight and different types
    class Unit(models.TextChoices):
        KILOGRAM = 'KG', 'Kilogram'
        CM = 'CM', 'Centimetre'

    unit = models.CharField(max_length=2, choices=Unit.choices)
    value = models.FloatField()
    part = models.ForeignKey(MeasureName, related_name='parts_names', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.part.name} - {self.value}'


class BodyMeasure(models.Model):
    measure = models.ForeignKey(Measure, related_name='measures', on_delete=models.SET_NULL, null=True)
