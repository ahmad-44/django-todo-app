from django.shortcuts import render
from .models import Task
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    # fetch the Todos for the User who have requested it
    tasks = Task.objects.filter(user_id=request.user.id).values()


    return render(request, 'index.html', {'tasks': tasks})