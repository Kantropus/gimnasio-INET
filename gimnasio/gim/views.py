from typing import ContextManager
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import GimLesson, GimClient, GimRoom
from .forms import LessonForm

def index(request):
    """The home page for the gim page."""
    return render(request, 'gimnasio/base.html')

def lessons(request):
    """Show list of available lessons."""
    Lessons = GimLesson.objects.filter()
    context = {'gimlessons':Lessons}
    return render(request, 'gimnasio/Clases.html', context)

@login_required
def clients(request):
    """Show all clients of the gym, only accesible to gym staff."""
    return render(request, 'gimnasio/Clientes.html')

#@login_required
def new_lesson(request,room_id):
    """Add a new lesson to 'lessons' table."""
    room = GimRoom.objects.get(id=room_id)
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = LessonForm()
    
    else:
        #Post data submitted; process data.
        form = LessonForm(data=request.POST)
        if form.is_valid():
            new_lesson = form.save(commit=False)
            new_lesson.room = room
            new_lesson.save()

        redirect('gimnasio:lessons')

    context = {'form': form, 'room': room}
    return render(request, 'gimnasio/new_lessons.html', context)