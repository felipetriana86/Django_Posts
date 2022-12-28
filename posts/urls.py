from django.urls import path, request
from posts import views

urlpatterns = [
    path('', views.home, name="homePage"),  
]
