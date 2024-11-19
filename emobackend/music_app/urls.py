from django.urls import path
from .views import detect_emotion  # Import the views module

urlpatterns = [
    # Add the emotion detection endpoint
    path('detect-emotion/',detect_emotion, name='detect-emotion'),
]
