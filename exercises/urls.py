from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.ExerciseListView.as_view(), name='exercises'),
]