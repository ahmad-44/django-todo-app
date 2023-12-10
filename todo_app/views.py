from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    # fetch the Todos for the User who have requested it
    tasks = Task.objects.filter(user_id=request.user.id).values()
    # print(tasks)
    return render(request, 'index.html', {'tasks': tasks})

@login_required(login_url='accounts/accounts/login') 
def create_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        if title:
            task = Task.objects.create(title = title, desc = desc, user_id = request.user.id)
            task.save()
            print('task created')
            return redirect('/')       
        else: 
            messages.info(request, 'Task Title Is Required')    

    
    return render(request, 'create_todo.html')

@login_required(login_url='accounts/accounts/login')
def view_todo(request):
    # fetch the id which comes in url like url?id=13
    id = request.GET.get('id', '') 
    #get the data of todo task which matches the ID
    task = Task.objects.filter(id=id).values() #
    #send the desired todo task to template
    return render(request, 'view_todo.html', {'task': task[0]})

@login_required(login_url='accounts/accounts/login')
def delete_todo(request):
    # fetch the id which comes in url like url?id=13
    id = request.GET.get('id', '') 
    #delete the object/
    Task.objects.filter(id=id).delete() #
    #send the desired todo task to template
    return redirect('/')

@login_required(login_url='accounts/accounts/login')
def complete_todo(request):
    # fetch the id which comes in url like url?id=13
    id = request.GET.get('id', '')
    Task.objects.filter(id=id).update(is_Task_Completed = True)
    return redirect('/')

@login_required(login_url='accounts/accounts/login')
def restart_todo(request):
    # fetch the id which comes in url like url?id=13
    id = request.GET.get('id', '')
    Task.objects.filter(id=id).update(is_Task_Completed = False)
    return redirect('/')

@login_required(login_url='accounts/accounts/login')
def edit_todo(request):
    if request.method == 'POST':
        id = request.POST['id']
        title = request.POST['title']
        desc = request.POST['desc']
        print(f"Title: {title}")
        if title:
            Task.objects.filter(id=id).update(title=title, desc=desc)    
            return redirect('/')       
        else: 
            messages.info(request, 'Task Title Is Required')
            return redirect(f'/edit_todo?id={id}&title={title}&desc={desc}')
    else:
        id = request.GET.get('id', '')
        title = request.GET.get('title', '')
        desc = request.GET.get('desc', '')
        task = {'id':id, 'title':title, 'desc':desc}
        # Task.objects.filter(id=id).update(is_Task_Completed = False)
        return render(request, 'edit_todo.html', {'task': task})

