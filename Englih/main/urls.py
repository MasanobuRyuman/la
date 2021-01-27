from django.urls import path
from . import views

app_name='main'
urlpatterns=[
    path('exercise', views.exercise, name='exercise'),
    path('move',views.move,name='move'),
    path('delete',views.delete,name='delete'),
    path('',views.IndexView.as_view(),name='index'),
    path('review',views.review,name='review'),
    path('index',views.Index2View.as_view(),name='index'),
]