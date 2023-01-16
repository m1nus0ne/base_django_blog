from django.urls import path, include
from django.contrib import admin
from .views import UserRegForm

urlpatterns = [
    path('register/', UserRegForm.as_view(), name = 'register'),

]