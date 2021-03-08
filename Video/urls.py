from .views import index, video_feed
from django.urls import path, include

app_name = 'video'

urlpatterns = [
    path('', index, name='index'),
    path('video_feed', video_feed, name='video_feed'),
]