from typing import ContextManager
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import GimLesson, GimClient, GimRoom, GimTeacher
from .forms import ClientForm, LessonForm, RoomForm, TeacherForm

def index(request):
    """The home page for the gim page."""
    return render(request, 'gim_page/base.html')

def lessons(request):
    """Show list of available lessons."""
    Lessons = GimLesson.objects.all()
    context = {'gimlessons': Lessons}
    return render(request, 'gim_page/Clases.html', context)

def rooms(request):
    """Show list of rooms, their type, size and location."""
    Rooms = GimRoom.objects.filter()
    context = {'rooms': Rooms}
    return render(request, 'gim_page/rooms.html', context)
#Only the gim staff can see the clients.
@login_required
def clients(request):
    """Show all clients of the gym, only accesible to gym staff."""
    return render(request, 'gim_page/clients.html')

#Only the gim staff can add a new lesson to de database.
@login_required
def new_lesson(request):
    """Insert lesson data"""
    form = LessonForm()
    
    if request.method == 'POST':
        #Post data submitted; process data.
        form = LessonForm(data=request.POST)
        if form.is_valid():
            """Add a new lesson to 'lessons' table."""
            form.save()

        return redirect('gim:lessons')

    context = {'form': form}
    return render(request, 'gim_page/new_lesson.html', context)

@login_required
def new_room(request):
    """Insert room data when a room is built."""
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(data=request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('gim:lessons')

    context = {'form': form}
    return render(request, 'gim_page/new_room.html', context)

@login_required
def new_teacher(request):
    """Insert teacher data."""
    form = TeacherForm()

    if request.method == 'POST':
        form = TeacherForm(data=request.POST)
        if form.is_valid():
            form.save()

        return redirect('gim:teachers')

    context = {'form': form}

    return render(request, 'gim_page/new_teacher.html', context)

def teachers(request):
    """Show list of rooms, their type, size and location."""
    Teachers = GimTeacher.objects.filter()
    context = {'teachers': Teachers}
    return render(request, 'gim_page/teachers.html', context)

def new_client(request):
    """Save client data."""
    form = ClientForm()

    if request.method == 'POST':
        form = ClientForm(data=request.POST)
        if form.is_valid():
            form.save()

        return redirect('gim:clients')

    context = {'form': form}

    return render(request, 'gim_page/clients.html', context)