from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            messages.info(request, f"This username {username} is already taken. Please try a new one.")
            print("SAME USERNAME ERROR")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            print("SAME EMAIL ERROR")
            messages.info(request, "There is an existing account on this email. Please try a new one.")
        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()
            print('User {username} created')
            auth.login(request, user)
            return redirect('/')
    return render(request, "register.html")


def logout(request): 
    auth.logout(request)
    return redirect('/')