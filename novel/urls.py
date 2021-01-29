from django.urls import path
from. import views

urlpatterns = [
     path('',views.index),
	 path('<str:character1>/<str:character2>/',views.my_novel)
         ]
