from django.urls import path
from tts.views import tts

urlpatterns=[
    path('',tts)
]