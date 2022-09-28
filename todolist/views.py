import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from todolist.models import Task
from todolist.forms import TaskForm

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user=request.user)
    context = {
        'list_data': data_todolist,
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

def create_task(request):
    if request.method == 'POST':
        task_create = TaskForm(request.POST)
        if task_create.is_valid():
            task_data = Task(
                user = request.user,
                date = datetime.datetime.now(),
                title = task_create.cleaned_data['nama'],
                description = task_create.cleaned_data['deskripsi']
            )
            task_data.save()
            messages.success(request, 'Task berhasil dibuat')
            return redirect('todolist:create_task')
    task_create = TaskForm()
    context = {'form':task_create}
    return render(request, 'create_task.html', context)