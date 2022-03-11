from unicodedata import name
from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

app_name = 'gim'

urlpatterns = [
    #Show the data
    path('', views.index, name='index'),
    path('lessons', views.lessons, name='lessons'),
    path('rooms', views.rooms, name='rooms'),
    path('teachers', views.teachers, name='teachers'),
    path('clients', views.clients, name='clients'),

    #Insert the data
    path('new_lesson', views.new_lesson, name='new_lesson'),
    path('new_room', views.new_room, name="new_room"),
    path('new_teacher', views.new_teacher, name='new_teacher'),
    path('new_client', views.new_client, name='new_client'),

    #Edit the data
    path('edit_lesson/<int:lesson_id>', views.edit_lesson, name='edit_lesson'),
    path('edit_room/<int:room_id>', views.edit_room, name='edit_room'),
    path('edit_teacher/<int:teacher_id>', views.edit_teacher, name='edit_teacher'),
    path('edit_client/<int:client_id>', views.edit_client, name='edit_client'),
]