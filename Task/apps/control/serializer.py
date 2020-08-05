from .models import *
from rest_framework import serializers

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
