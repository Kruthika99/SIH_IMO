from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name ='index'),
    path('home',views.index,name ='index'),
    path('login',views.login,name='login'),
    path('register',views.reg,name='register'),
    path('portal',views.portal,name='portal')
]
