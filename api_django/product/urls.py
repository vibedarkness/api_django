from django.urls import path

from .views import api_views_vibe


urlpatterns = [
    path('',api_views_vibe,name='vibe_api'),
]
