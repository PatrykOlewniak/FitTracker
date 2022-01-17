from django.db import models
from django.utils.translation import gettext as _


class Exercise(models.Model):
    class MuscleGroup(models.TextChoices):
        SHOULDERS = 'SHOULDERS', _('Shoulders - Rotator Cuff')
        LEGS_H = 'LEGS_H', _('Legs - Hamstrings')
        ABDOMINALS_T = 'ABDOMINALS_T', _('Abdominals - Total')
        ABDOMINALS_L = 'ABDOMINALS_L', _('Abdominals - Lower')
        LEGS_Q = 'LEGS_Q', _('Legs - Quadriceps')
        BICEPS = 'BICEPS', _('Biceps')
        SHOULDERS_D = 'SHOULDERS_D',  _('Shoulders - Delts/Traps')
        BACK = 'BACK', _('Back - Latissimus Dorsi')
        ABDOMINALS_U = 'ABDOMINALS_U', _('Abdominals - Upper')
        ABDOMINALS_O = 'ABDOMINALS_O', _('Abdominals - Obliques')
        BACK_LAT_RHO = 'BACK_LAT_RHO', _('Back - Lat.Dorsi/Rhomboids')
        CALVES_SOL = 'CALVES_SOL', _('Calves - Soleus')
        CALVES_GAST = 'CALVES_GAST', _('Calves - Gastrocnemius')
        LOWER = 'LOWER', _('Lower Back - Erector Spinae')
        TRICEPS = 'TRICEPS', _('Triceps')
        CHEST = 'CHEST', _('Chest - Pectoralis')
        NOT_KNOWN = 'NOT_KNOWN', _('Not known')

    class Level(models.IntegerField):
        BEGINNER = 1, 'beginner'
        INTERMEDIATE = 2, 'intermediate'
        ADVANCED = 3, 'advanced'

    class BodyPart(models.TextChoices):
        LOWER = 'Lower'
        UPPER = 'Upper'
        CORE = 'Core'

    class Modality (models.TextChoices):
        FW = 'FW', 'Free Weights'
        C = 'Cables', 'Cables'
        M = 'Machine', 'Machine'

    class Joint(models.TextField):
        MULTI = 'Multi-Joint Exercise'
        SINGLE = 'Single-Joint Exercise'

    name = models.TextField(max_length=255)
    muscle_group = models.TextField(
        max_length=255, choices=MuscleGroup.choices, default=MuscleGroup.NOT_KNOWN
    )
