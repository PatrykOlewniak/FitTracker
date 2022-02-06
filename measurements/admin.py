from django.contrib import admin
from .models import *

# TODO: change default user field for MeasureName (Django cant find a user with id 0 (treats null like 0)
admin.site.register(MeasureName)
admin.site.register(Measure)
admin.site.register(BodyMeasure)