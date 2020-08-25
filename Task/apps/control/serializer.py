from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from django.db import models



#Usuario
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','url', 'username', 'email', 'groups','first_name','last_name']
        

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

#Usuario

#Perfil de usuario
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserProfile
        fields = '__all__'




class projectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = project
        fields = '__all__'




class kambanSerializer(serializers.ModelSerializer):
    class Meta:
        model = kamban
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    #owner = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'




##Seccion para agregar informacion###
class CommentAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


##Archivos que son subidos por comentarios
class Comment_FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment_File
        fields = '__all__'


class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = members
        fields = '__all__'


class MembersDetailSerializer(serializers.ModelSerializer):
    member = UserSerializer()
    class Meta:
        model = members
        fields = '__all__'


