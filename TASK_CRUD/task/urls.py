from django.urls import path
from .views import user_note,add_task,get_note,modify_task

urlpatterns=[
    path('<str:user>',user_note,name='User Notes List'),
    path('task/<str:user>/<int:note>',add_task,name='Task actions'),
    path('note/<str:user>/<int:note>',get_note,name='Note actions'),
    path('task/<str:user>/<int:note>/<int:id>',modify_task,name='Modificaiton Task actions'),
]