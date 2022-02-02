from django.contrib import admin
from django.urls import path, include

app_name = 'gim'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gim.urls')),
    path('users/', include('users.urls')),
]
