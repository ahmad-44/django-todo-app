from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    # fetch the Todos for the User who have requested it
    tasks = Task.objects.filter(user_id=request.user.id).values()


    return render(request, 'index.html', {'tasks': tasks})

@login_required(login_url='/') 
def create_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
    
        task = Task.objects.create(title = title, desc = desc, user_id = request.user.id)
        task.save()
        print('task created')
        return redirect('/')
    
    return render(request, 'create_todo.html')



