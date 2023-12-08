from django.shortcuts import render
from .models import Task
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    # fetch data in form of queryset
    tasks = Task.objects.filter(user_id='2').values()

    # convert that data into a dict
    my_dict = {}

    for index, element in enumerate(tasks):
        my_dict[index] = element


    return render(request, 'index.html', {'tasks': tasks})