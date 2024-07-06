from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('audioindex', views.audioindex, name='audioindex'),
    path('home', views.home, name='home'),
    path('process_audio/', views.process_audio, name='process_audio'),
]