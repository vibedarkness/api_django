from django.urls import path

from .views import api_views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('',api_views,name='api_views'),
    path('auth',obtain_auth_token),
    
]
