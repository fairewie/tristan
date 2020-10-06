from django.urls import path
from . import views 

urlpatterns =[
    path('task',views.La_Task,name='task'),
    path('user',views.Le_User,name='user'),
    path('edit/<int:param>', views.edit, name='edite'),
    path('listing',views.task_listing,name='listing'),
    path('userlisting',views.user_listing,name='listing'),
    path('del/<int:pers_id>', views.delete, name='delete'),
    path('deletetask/<int:pers_id>', views.deletetask, name='deletetask'),
    path('taskedit/<int:param>', views.taskedit, name='taskedite'),

    
    ]
