from django.urls import path
from. import views

urlpatterns = [
     path('',views.index),
     path('test', views.test),
     path('signup', views.signup),
     path('schedule', views.schedule),
     path('git', views.git),
     path('gugu', views.gugu),
     path('login', views.login),
     path('menu', views.menu)
         ]

