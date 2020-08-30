from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler400, handler403, handler404, handler500
from django.conf import settings
from django.conf.urls.static import static
from .views import *



app_name='base'


urlpatterns = [
    path('', Index, name='index'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/',signup, name='signup'),
    path('signup/',signup, name='signup'),
    #path('notificar/',send_message_to_all_users, name='notifi'),
    path('save_token/',guardar_token , name='guardar_token')
    

]

