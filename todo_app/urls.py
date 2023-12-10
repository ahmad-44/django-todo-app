from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_todo", views.create_todo, name="create_todo"),
    path("view_todo", views.view_todo, name="view_todo"),
    path("delete_todo", views.delete_todo, name="delete_todo"),
    path("complete_todo", views.complete_todo, name="complete_todo"),
    path("restart_todo", views.restart_todo, name="restart_todo"),
    path("edit_todo", views.edit_todo, name="edit_todo")

]
