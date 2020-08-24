from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(project)
admin.site.register(members)
admin.site.register(kamban)
admin.site.register(Task)
admin.site.register(Assigned)
admin.site.register(SubTask)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(Comment_File)

