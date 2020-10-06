from django.contrib import admin
from lemyModel.models import Task,User

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display=('utilisateur',"task_name",'release_date')
admin.site.register(Task,TaskAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display=('first_name',"last_name")
admin.site.register(User,UserAdmin)
