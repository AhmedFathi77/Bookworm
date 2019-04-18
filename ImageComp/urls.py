
from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('' , views.text_image_view, name='Upload'),
    path('/success/' , views.success.as_view(), name='success')
]
