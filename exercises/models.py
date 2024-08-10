from django.db import models
from django.urls import reverse


from django.conf import settings
User = settings.AUTH_USER_MODEL


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='excersise_images', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('exercise-detail', kwargs={'pk': self.pk})


class Training(models.Model):
    date = models.DateTimeField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercises = models.ManyToManyField(Exercise, related_name='trainings')


class Set(models.Model):
    repetitions = models.IntegerField()
    weight = models.FloatField()
    training = models.ForeignKey(Training, related_name='sets', on_delete=models.CASCADE)

