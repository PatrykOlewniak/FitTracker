import django_filters
from .models import Exercise


class ExerciseFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Exercise
        fields = ['name', 'muscle_group', 'level', 'body_part', 'modality', 'joint']
