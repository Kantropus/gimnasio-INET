from django import forms
from .models import GimLesson

"""Forms used by the gim staff to create data."""

class LessonForm(forms.ModelForm):
    """A form for the admin to create a lesson."""
    class Meta:
        model = GimLesson
        fields = ['description','datetime','room']

        