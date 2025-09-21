from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='webcode'),
    path('start-wipe/', views.start_wipe, name='webcode'),
]