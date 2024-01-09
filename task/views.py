from django.shortcuts import get_object_or_404,render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import CustomUser,Task

# Create your views here.
def Home(request):
    return render(request, 'home.html')

def Register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if confirm_password == password:
            CustomUser.objects.create_user(username=username, password=password)
            return redirect('login')
        else:
             error_message = "Passwords do not match."
             return render(request, 'registration.html', {'error_message': error_message})

    return render(request, 'register.html')

def UserLogin(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(request, username=username ,password=password)
        if user is not None:
            login(request, user)
            return redirect('header')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login credentials!'}) 

    return render(request, 'login.html')

def UserLogOut(request):
    logout(request)
    return redirect('login')


@login_required
def Header(request):
    user_name = request.user.get_username()
    return render(request, 'header.html', {'user_name': user_name} )


@login_required
def AddTask(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        current_user = request.user
        data = Task(title=title, description=description, user=current_user)
        data.save()
        
    return render(request, 'add_task.html')

@login_required
def Tasks(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks.html',  {'tasks': tasks})

@login_required
def DeleteTask(request,task_id):
     task = get_object_or_404(Task, pk=task_id)
     task.delete()

     return redirect('tasks')

@login_required
def EditTask(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == "POST":
        task.title = request.POST.get('title', '')
        task.description = request.POST.get('description', '')

        task.save()

        return redirect('tasks')
    return render(request, 'edit_task.html', {'task': task})


