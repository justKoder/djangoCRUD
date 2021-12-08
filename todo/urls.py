from django.urls import path
from . import views

urlpatterns = [
    path('', views.allTodos, name='allTodos'),
    path('add-todo', views.createTodo, name='createTodo'),
    path('edit-todo/<int:todoID>', views.editTodo, name='editTodo'),
    path('delete-todo/<int:todoID>', views.deleteTodo, name='deleteTodo'),
]
