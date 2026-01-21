from django.urls import path
from . import views

app_name = 'Characters'

urlpatterns = [
    path('', views.character_list, name='character_list'),
]