from django.urls import path
from . import views

urlpatterns = [
    path("accounts/register", views.register, name="register"),
    path("accounts/login", views.login, name="login"),
    path("logout", views.logout, name="logout")
]
