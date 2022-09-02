from django.urls import path

from .import views 


urlpatterns=[
    path('',views.SearchListViews.as_view(), name='search'),
    
]