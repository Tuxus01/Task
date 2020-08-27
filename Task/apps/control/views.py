import os
import sys
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from .models import *
from rest_framework import viewsets, permissions, filters
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
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory


#JSON API
from django.http import JsonResponse


#Login
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView
import Task.settings as setting

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from django.core.files import File

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            #agregando imagen al perfil de usuario
            profile = UserProfile()
            profile.user = user

            
            path='perfil.png'
            profile.image = File(open(path, 'rb'))
            profile.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignUpForm()
    return render(request, 'base/signup.html', {'form': form})





class LoginFormView(LoginView):
    template_name = 'base/login.html'
    success_url = reverse_lazy('base:index')
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(setting.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context

class LogoutRedirectView(RedirectView):
    pattern_name = 'login'
    success_url = reverse_lazy('base:login')
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)



# Create your views here.
@login_required(login_url='/login/')
def Index(request):
    foto = UserProfile.objects.get(user=request.user)
    print(foto)
    ctx ={ 'IMAGE': foto }
    return render(request, 'base/index.html' ,ctx)



#Extraer Usuario del la base de datos.
#Usuario
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import permission_required
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth.models import User, Group


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    search_fields = ['=username']
    filter_backends = (filters.SearchFilter,)
    


class GroupViewSet(viewsets.ModelViewSet):
    
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


#Usuario




#Listado de projectos en los que estoy trabajando
class projectViewSet(viewsets.ModelViewSet):
    queryset = project.objects.all()
    serializer_class = projectSerializer
    filter_fields = ('code',)
    #Extraccion de solo los projectos activo en los que estoy trabajando
    def list(self, request):
        list_ = members.objects.filter(member=request.user)
        
        #list_ = members.objects.all()
        #print(list_)
        #Ciclo que recolecta y agraga a la lista visual del html los project activos en los que estoy laborando
        projecto_list = []
        for i in list_:
            pro = project.objects.get(pk=i.project.id)
            #Validacion de project activo
            if pro.status == True:
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
        #list_task = Task.objects.filter(kamban=id_kamban).filter(status=True)
        list_task = Task.objects.filter(kamban=id_kamban)
        print(list_task)
        queryset = list_task
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)
        



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-id')
    serializer_class = CommentSerializer
    #filter_fields = ('code',)
    search_fields = ['task__id']
    filter_backends = (filters.SearchFilter,)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    #filter_fields = ('code',)
    search_fields = ['user__id']
    filter_backends = (filters.SearchFilter,)

    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    #filter_fields = ('code',)
    #search_fields = ['task__id']
    #filter_backends = (filters.SearchFilter,)



##Seccion para agregar informacion###
class CommentAddViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-id')
    serializer_class = CommentAddSerializer
    

class Comment_FileViewSet(viewsets.ModelViewSet):
    queryset = Comment_File.objects.all().order_by('-id')
    serializer_class = Comment_FileSerializer
    search_fields = ['comment__id']
    filter_backends = (filters.SearchFilter,)


class MembersViewSet(viewsets.ModelViewSet):
    queryset = members.objects.all().order_by('-id')
    serializer_class = MembersSerializer
    search_fields = ['=project__id','=member__id']
    filter_backends = (filters.SearchFilter,)


class MembersDetailViewSet(viewsets.ModelViewSet):
    queryset = members.objects.all().order_by('-id')
    serializer_class = MembersDetailSerializer
    search_fields = ['project__id']
    filter_backends = (filters.SearchFilter,)