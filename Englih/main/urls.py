from django.urls import path
from . import views

app_name='main'
urlpatterns=[
    path('exercise', views.exercise, name='exercise'),
    path('move',views.move,name='move'),
    path('',views.IndexView.as_view(),name='index'),
]