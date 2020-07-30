from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from datetime import date
from datetime import datetime
from django.forms import model_to_dict






#Base Global para todas las tablas
class ModelBase(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField('Status', default=True)
    date_create = models.DateField('Date of Create',auto_now = False, auto_now_add = True)
    date_change = models.DateField('Date of Change',auto_now = True, auto_now_add = False)
    date_delete = models.DateField('Date of Delete',auto_now = True, auto_now_add = False)
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    date_time_c = models.TimeField(auto_now = False, auto_now_add = True)
    date_time_m = models.TimeField(auto_now = True, auto_now_add = False)

    class Meta:
        abstract = True


'''
-Proyecto
al crear el proyecto el administrador podra asignar @personal al grupo de trabajo de las cuales seran los unicos que podran 
visualizar lo que cotiene el mismo.


    -User
        
    -Kamban 
        -Creacion del los proceso de Kamba para las tareas
            -Inicio, Proceso, Evaluacion, Finalizado - Ejm

    

    -Wiki
        -Documentacion del proyecto
        Lave(TAKS)


    -Taks - (TO DO LIST)
        -Task_asignacion(User)
            -Comentarios (IDTASK, IDSUBTASK)
            -Task_Sub_task
                -SubTask - Comentario
                -SubTask - Files
        
            -Task_files
        -Task_Kanban = (Kamban)
        -Task_Date_Finalizacion = control de tiempo
        -Task_Date_Inicio = Fecha configurada manualemtne de inicio de la tarea
        -Task_Recordatorio (Programar envio de recordatorio)

        



'''

class project(ModelBase):
    name = models.CharField('Name Kamban Step',max_length=80, unique=True) #Nombre del proyecto a trabajar
    description = models.TextField(max_length=600, blank=True, null=True)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return self.name 



class members(ModelBase):
    project = models.ForeignKey(project, on_delete=models.CASCADE) #Project relacionado con el paso del kamban
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner' ,blank=True, null=True)

    def __str__(self):
        return self.member.username
    



class kamban(ModelBase):
    name = models.CharField('Kamban Step',max_length=80, unique=True) #Inicio, proceso, finalizado
    description = models.TextField(max_length=600, blank=True, null=True)
    project = models.ForeignKey(project, on_delete=models.CASCADE) #Project relacionado con el paso del kamban

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return self.name 


class Task(ModelBase):
    title = models.CharField('task',max_length=80) #Titulo de la tarea
    project = models.ForeignKey(project, on_delete=models.CASCADE) #Project relacionado
    kamban = models.ForeignKey(kamban, on_delete=models.CASCADE, blank=True, null=True) #Paso actual del kamba

    def __str__(self):
        return self.title


class Assigned(ModelBase):
    assigned = models.ForeignKey(members, on_delete=models.CASCADE, blank=True, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.assigned


class SubTask(ModelBase):
    title = models.CharField('task',max_length=80) #Titulo de la tarea
    task = models.ForeignKey(Task,on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Comment(ModelBase):
    comment = models.TextField(max_length=1500)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, blank=True, null=True)
    subtask = models.ForeignKey(SubTask, on_delete=models.CASCADE, blank=True, null=True)

