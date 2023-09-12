from django.urls import path
from . import views

app_name = 'question'

urlpatterns = [
    path('hello_world/', views.hello_world, name='hello_world'),
    path('create/', views.question_create, name='create'),
]
