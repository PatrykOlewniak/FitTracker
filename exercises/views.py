from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView

from .forms import ExerciseForm
from .models import Exercise, Training


# def new_exercise(request):
#     if request.method == 'POST':
#         form = ExerciseForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('exercises_list')
#     else:
#         form = ExerciseForm()
#     return render(request, 'exercises/new_exercise.html', {'form': form})
#

class ExerciseCreateView(CreateView):
    model = Exercise
    fields = ['name', 'description', 'image']
    template_name = 'exercises/exercise_form.html'
    success_url = reverse_lazy('exercises_list')


class ExerciseDetailView(DetailView):
    model = Exercise
    template_name = 'exercises/exercise_detail.html'

class ExerciseListView(ListView):
    model = Exercise
    template_name = 'exercises/exercise_list.html'
    context_object_name = ('exercises')


class ExerciseDeleteView(DeleteView):
    model = Exercise
    template_name = 'exercises/exercise_confirm_delete.html'
    success_url = reverse_lazy('exercises_list')


class ExerciseUpdateView(UpdateView):
    model = Exercise
    fields = ['name', 'description', 'image']
    template_name = 'exercises/exercise_update.html'
    success_url = '/exercises/'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.image = self.request.FILES.get('image')
        return super().form_valid(form)


class TrainingCreateView(CreateView):
    model = Training
    fields = ['user', 'exercises']
    template_name = 'trainings/training_form.html'
    success_url = '/trainings/'

    def form_valid(self, form):
        form.instance.date = timezone.now()
        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user
        return initial


class TrainingUpdateView(UpdateView):
    model = Training
    fields = ['date', 'user', 'exercises']
    template_name = 'trainings/training_update.html'
    success_url = reverse_lazy('trainings_list')


class TrainingDeleteView(DeleteView):
    model = Training
    template_name = 'trainings/training_confirm_delete.html'
    success_url = reverse_lazy('trainings_list')


class TrainingDetailView(DetailView):
    model = Training
    template_name = 'trainings/training_detail.html'



class TrainingListView(ListView):
    model = Training
    template_name = 'trainings/training_list.html'
    context_object_name = 'trainings'



