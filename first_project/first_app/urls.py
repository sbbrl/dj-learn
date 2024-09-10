from django.contrib import admin
from django.urls import path, include
from first_app import views


urlpatterns = [
    path('',views.index,name="index"),
    path('home/',views.home,name="home"),
    path('educative/',views.educative,name="educative"),
    path('hello/<str:name>/',views.hello,name="hello"),
    path('eod/<int:num>/',views.eod,name="eod")
    ]