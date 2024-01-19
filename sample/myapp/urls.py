from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # name lets you reference to the URL with just the name!
]
