from django.contrib import admin
from django.urls import path, re_path

from menu.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('institutions/schools/music/', index, name='music-school'),
    path('institutions/schools/sport/', index, name='sport-school'),
    re_path(r'.*', index),
]
