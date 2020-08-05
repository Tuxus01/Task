from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from .models import *

from django.utils import timezone
from django.contrib.auth.decorators import permission_required

#Login
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView
from django.contrib.auth.models import User

from rest_framework import viewsets
from django.db.models import Prefetch
from .models import *
from .serializer import *
from rest_framework.response import Response


#JSON API
from django.http import JsonResponse


# Create your views here.
def Index(request):
    return render(request, 'base/index.html' )

#Listado de projectos en los que estoy trabajando
class projectViewSet(viewsets.ModelViewSet):
    queryset = project.objects.all()
    serializer_class = projectSerializer
    filter_fields = ('code',)
    #Extraccion de solo los projectos activo en los que estoy trabajando
    def list(self, request):
        list_ = members.objects.filter(member=request.user)
        #print(list_)
        #Ciclo que recolecta y agraga a la lista visual del html los project activos en los que estoy laborando
        projecto_list = []
        for i in list_:
            pro = project.objects.get(pk=i.project.id)
            #Validacion de project activo
            #if pro.status == True:
            projecto_list.append(pro)
        
        #print(projecto_list)
        #queryset = project.objects.filter(owner=request.user)
        #Enviamos al queryset por medio de array los project 
        queryset = projecto_list
        serializer = projectSerializer(queryset, many=True)
        return Response(serializer.data)

    #Proceso de extraccion de Kamban por ID de Prjecto, este proceso automatizara las consultas 
    #Mostrara Kamban, y Taks dentro de cada uno de los pasos
    def retrieve(self, request,  *args, **kwargs):

        #Capturando el ID del proyecto
        id_projecto = kwargs.get('pk')
        
        #Buscar los Kamban por medio del id del projecto
        kam = kamban.objects.filter(project=id_projecto)

        serializer = kambanSerializer(kam, many=True)
        return Response(serializer.data)



#Listado de Kamban por Projecto en los que estoy trabajando
class kambanViewSet(viewsets.ModelViewSet):
    queryset = kamban.objects.all()
    serializer_class = kambanSerializer
    filter_fields = ('code',)
    

    def retrieve(self, request,  *args, **kwargs):
        id_kamban = kwargs.get('pk')
        list_task = Task.objects.filter(kamban=id_kamban)
        print(list_task)
        queryset = list_task
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)
        
