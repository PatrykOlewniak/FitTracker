from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from exercises.views import ExerciseListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('exercises/', include('exercises.urls')),
    path('', ExerciseListView.as_view(), name='exercises:exercises_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
