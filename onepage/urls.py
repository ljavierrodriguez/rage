from django.urls import path

from onepage import views

urlpatterns = [
    path('', views.home, name="home")
]