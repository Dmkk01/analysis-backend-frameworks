from django.urls import path

from . import views

urlpatterns = [
    path('', views.health, name='health'),
    path('hello/', views.hello, name='hello'),
    path('fibonacci/', views.fibonacci, name='fibonacci')
]