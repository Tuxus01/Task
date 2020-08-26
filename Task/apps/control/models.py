from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from datetime import date
from datetime import datetime
from django.forms import model_to_dict
from django.contrib.auth.models import AbstractUser
from datetime import date
from datetime import datetime






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
        return self.project.name + " - " + self.name 


class Task(ModelBase):
    title = models.CharField('task',max_length=80) #Titulo de la tarea
    project = models.ForeignKey(project, on_delete=models.CASCADE) #Project relacionado
    kamban = models.ForeignKey(kamban, on_delete=models.CASCADE, blank=True, null=True) #Paso actual del kamba
    priority = models.IntegerField(choices=((1,("Low")),(2,("Medium")),(3,("Urgent")),(4,("Wait"))),default=1)
    description = models.TextField(max_length=3000, blank=True, null=True)

    def __str__(self):
        return self.title


class Assigned(ModelBase):
    assigned = models.ForeignKey(members, on_delete=models.CASCADE, blank=True, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.assigned.member.username


class SubTask(ModelBase):
    title = models.CharField('task',max_length=80) #Titulo de la tarea
    task = models.ForeignKey(Task,on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Comment(ModelBase):
    comment = models.TextField(max_length=1500)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, blank=True, null=True)
    subtask = models.ForeignKey(SubTask, on_delete=models.CASCADE, blank=True, null=True)


#Extendiendo el modelo de USER para poder agregar contenido adicional al perfil

def Profile_file(self,filename):
    today = date.today()
    year = format(today.year)
    mes = format(today.month)
    dia = format(today.day)
    path = "static/MultimediaData/img/%s/%s/%s/%s/%s" %(str(year), str(mes), str(dia), str(self.user.username), str(filename))
    return path


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=Profile_file, blank=True, null=True)

    def __str__(self):
        return self.user.username


def File_comment(self, filename):
    path = "static/MultimediaData/comment/%s/%s" %(str(self.comment.task.project.name),  str(filename))
    return path

#Almacenara los archivos multimedia de los comentarios agregados
class Comment_File(ModelBase):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    files = models.FileField(upload_to=File_comment)

    def __str__(self):
        return self.comment.comment


