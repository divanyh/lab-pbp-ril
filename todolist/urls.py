from multiprocessing.util import is_abstract_socket_namespace
from django.urls import path
from todolist.views import show_todolist
from todolist.views import login_user
from todolist.views import add_task
from todolist.views import logout_user
from todolist.views import register
from todolist.views import show_json
from todolist.views import quick_add_task
from todolist.views import delete_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('login/', login_user, name='login_user'),
    path('create-task', add_task, name='add_task'),
    path('logout/', logout_user, name='logout_user'),
    path('register/', register, name='register'),
    path('json/', show_json, name='show_json'),
    path('add/', quick_add_task, name='quick_add_task'),
    path('delete/<id>', delete_task, name='delete_task')
]