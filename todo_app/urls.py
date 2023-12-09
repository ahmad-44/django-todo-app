from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_todo", views.create_todo, name="create_todo")
]
