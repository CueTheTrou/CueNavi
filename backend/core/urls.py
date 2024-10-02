from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import MusicFileUploadView

urlpatterns = [
    path('upload/', MusicFileUploadView.as_view(), name='music-upload'),
]