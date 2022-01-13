from django.contrib import admin
from .models import GimRoom, GimLesson, GimTeacher, GimClient
# Register your models here.

admin.site.register(GimRoom)
admin.site.register(GimLesson)
admin.site.register(GimTeacher)
admin.site.register(GimClient)
