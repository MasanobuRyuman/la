from django.urls import path
from . import views

app_name='main'
urlpatterns=[
    path('',views.formView.as_view(),name='form'),
    path('exercise', views.exercise, name='exercise'),
    path('move',views.move,name='move'),
    path('delete',views.delete,name='delete'),
    path('next',views.next,name='next'),
    path('change',views.change,name='change'),
    path('review',views.review,name='review'),
    path('test',views.test,name='test'),
    path('index',views.Index2View.as_view(),name='index'),
    path('login',views.login,name='login'),
    path('newlogin',views.newlogin,name='newlogin'),
]
