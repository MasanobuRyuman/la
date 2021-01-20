from django.urls import path
from . import views

app_name='main'
urlpatterns=[
    path('exercise', views.exercise, name='exercise'),
    path('',views.IndexView.as_view(),name='index'),
]