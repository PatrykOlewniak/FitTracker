from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from tools.views import FilteredListView
from .filters import ExerciseFilter
from .models import Exercise


class ExerciseListView(FilteredListView):
    model = Exercise
    filterset_class = ExerciseFilter


class CreateExercise(CreateView):
    model = Exercise
    fields = (
        'name', 'muscle_group', 'level', 'body_part', 'modality', 'joint'
    )
    success_url = reverse_lazy('exercises-list')


class UpdateExercise(UpdateView):
    model = Exercise
    fields = (
        'name', 'muscle_group', 'level', 'body_part', 'modality', 'joint'
    )


