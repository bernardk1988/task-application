from django.urls import path
from . import views

urlpatterns = [
    # Website URLs
    path("", views.todo_list, name="todo_list"),
    path("add_todo/", views.add_todo, name="add_todo"),
    path("edit_todo/<int:pk>/", views.edit_todo, name="edit_todo"),

    # REST API URLs
    path("api/todos/", views.todo_api, name="todo_api"),
    path("api/todos/add/", views.add_todo_api, name="add_todo_api"),
    path("api/todos/update/<int:pk>/", views.update_todo_api, name="update_todo_api"),
    path("api/todos/delete/<int:pk>/", views.delete_todo_api, name="delete_todo_api"),
]


