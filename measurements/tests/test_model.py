from django.test import TestCase
from measurements.models import MeasureName


class CreateMeasureTest(TestCase):

    def test_create_measure_name_without_user(self):
        MeasureName.objects.create(name='test_name1', generic=True)
        assert MeasureName.objects.get(name='test_name1').user is None