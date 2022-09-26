from django.urls import path
from todolist.views import show_todolist
from todolist.views import login_user

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('login/', login_user, name='login_user'),
    path('create-task/'),
    path('logout/')
]