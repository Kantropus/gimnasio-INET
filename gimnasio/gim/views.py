from typing import ContextManager
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import GimClass, GimClient

def index(request):
    """The home page for the gim page."""
    return render(request, 'gimnasio/base.html')

def classes(request):
    """Show list of available classes."""
    context = GimClass.objects.get()
    return render(request, 'gimnasio/Clases.html', context)

@login_required
def clients(request):
    """Show all clients of the gym, only accesible to gym staff."""
    return render(request, 'gimnasio/Clientes.html')