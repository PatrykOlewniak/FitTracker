from django.urls import path
from .views import ExerciseListView, ExerciseUpdateView, ExerciseDetailView, \
    ExerciseDeleteView, ExerciseCreateView, TrainingCreateView, TrainingListView, \
    TrainingUpdateView, TrainingDetailView, TrainingDeleteView

urlpatterns = [
    path('new_exercise/', ExerciseCreateView.as_view(), name='exercise_new'),
    path('', ExerciseListView.as_view(), name='exercises_list'),
    path('edit_exercise/<int:pk>/', ExerciseUpdateView.as_view(), name='edit_exercise'),
    path('exercise/<int:pk>/', ExerciseDetailView.as_view(), name='exercise_detail'),
    path('exercise/<int:pk>/delete/', ExerciseDeleteView.as_view(), name='exercise_delete'),
    path('new_training/', TrainingCreateView.as_view(), name='training_new'),
    path('trainings/', TrainingListView.as_view(), name='trainings_list'),
    path('edit_training/<int:pk>/', TrainingUpdateView.as_view(), name='edit_training'),
    path('training/<int:pk>/', TrainingDetailView.as_view(), name='training_detail'),
    path('training/<int:pk>/delete/', TrainingDeleteView.as_view(), name='training_delete'),
]