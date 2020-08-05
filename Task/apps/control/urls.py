from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler400, handler403, handler404, handler500
from django.conf import settings
from django.conf.urls.static import static
from .views import *



app_name='base'


urlpatterns = [
    path('', Index, name='index'),
]

