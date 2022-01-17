from tools.views import FilteredListView

from .filters import ExerciseFilter
from .models import Exercise


class ExerciseListView(FilteredListView):
    model = Exercise
    filterset_class = ExerciseFilter
