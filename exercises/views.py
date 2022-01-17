from django.http import HttpResponse
from django.views import generic

from .models import Exercise


def index(request):     # TEST view
    ex_list = Exercise.objects.all()
    output = '\n'.join(['<br>'.join((q.name, q.muscle_group)) for q in ex_list])
    return HttpResponse(output)


class ExerciseListView(generic.ListView):
    model = Exercise