from binascii import rledecode_hqx
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
import datetime
from todolist.models import Task
from .forms import CreateTaskForm


# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    # data_todolist = Task.objects.filter(user__isequal = )
    # data_todolist = Task.objects.get(pk = user_id)
    data_todolist = Task.objects.filter(user = request.user)
    context = {
        'data': data_todolist,
        'username': request.COOKIES['username']
    }
    # print(request.COOKIES['username'])
    return render(request, 'todolist.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('todolist:show_todolist'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            response.set_cookie('username', username)
            return response
        else:
            messages.info(rledecode_hqx, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login_user')

    context = {'form':form}
    return render(request, 'register.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login_user'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def show_json(request):
    data = Task.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data))

# def add_task(request):
#     if(request.POST):
#         newTask = Task(user = request.user, title = request.POST.get('title'), description = request.POST.get('description'), date_created = datetime.date.today())
#         newTask.save()
#         # form = CreateTaskForm(request.POST)
#         # # response = {'form' : form} 
#         # if (form.is_valid()):
#         #     form.save()
#         # form_data = form.cleaned_data
#         # # response = HttpResponseRedirect(reverse('todolist:show_todolist'))
#         # # response.set_cookie('date_created', str(datetime.datetime.now()))
#         # new_task = Task()
#         # new_task.date = str(datetime.datetime.now())
#         # new_task.title = form_data.get('title')
#         # new_task.description = form_data.get('description')
#         # # task = Task(date = str(datetime.datetime.now()), )
#         return redirect('todolist:show_todolist')
#     # else:
#     #     form = CreateTaskForm()
#     return render(request, 'create-task.html')

def add_task(request):
    submitted = False
    if(request.POST):
        form = CreateTaskForm(request.POST)
        # # response = {'form' : form} 
        if (form.is_valid()):
            task = form.save(commit=False)
            task.user = request.user
            task.save()
        # form_data = form.cleaned_data
            response = redirect('todolist:show_todolist')
            return response
        else:
            form = CreateTaskForm
            if 'submitted' in request.GET:
                submitted = True
    return render(request, 'create-task.html')

def quick_add_task(request):
    if(request.POST):
        task_title = request.POST.get('title')
        task_desc = request.POST.get('description')
        task_date = datetime.datetime.now()
        task_user = request.user

        new_task = Task(title = task_title, description = task_desc, date_created = task_date, user = task_user)
        new_task.save()
        return HttpResponse(b"CREATED", status = 201)
    return HttpResponseNotFound()

def delete_task(request, id):
    context = {}
    task = get_object_or_404(Task,pk = id)
    
    if(request.POST):
        task.delete()
        return HttpResponse(b"DELETED", status = 201)
    return HttpResponseNotFound()

