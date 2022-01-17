from django import forms
from django.forms import fields
from .models import GimClient, GimLesson, GimRoom, GimTeacher

"""Forms used by the gim staff to create data."""

class LessonForm(forms.ModelForm):
    """A form for the admin to create a lesson."""
    class Meta:
        model = GimLesson
        fields = ['description','datetime','room','price','teacher']

class RoomForm(forms.ModelForm):
    """A form to call when setting up te data for a new room in the gim."""

    class Meta:
        model = GimRoom
        fields = ['location','area','room_type']

class TeacherForm(forms.ModelForm):
    """Teacher information, they do not have access to the database, thus, they're not users."""
    class Meta:
        model = GimTeacher
        fields = ['dni', 'first_name', 'last_name', 'phone_number', 'birthdate', 'hiring_date']

class ClientForm(forms.ModelForm):
    class Meta:
        model = GimClient
        fields = ['affiliate_number', 'profession', 'first_name', 'last_name', 'address', 'phone_number', 'is_up_to_date']