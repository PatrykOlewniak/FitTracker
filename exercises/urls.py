from django.urls import path, reverse

from . import views

urlpatterns = [
    path('', views.ExerciseListView.as_view(), name='exercises-list'),
    path('create/', views.CreateExercise.as_view(), name='create-exercise'),
    path('edit/<int:pk>/', views.UpdateExercise.as_view(success_url="/exercises/"), name='edit-exercise')
]
