from django.shortcuts import redirect, render
from django import forms
from django.http import HttpResponseRedirect, HttpResponse

import todo
from .models import Todo
# Create your views here.


def allTodos(request):
    tasks = Todo.objects.all()
    data = {
        'tasks': tasks,
    }
    return render(request, 'todo.html', data)


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['todo', 'scheduled']

        widgets = {
            'todo': forms.TextInput(attrs={'class': 'form-control'}),
            'scheduled': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }


def createTodo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Successfully saved')
    else:
        form = TodoForm()
    return render(request, 'form.html', {'form': form})


def editTodo(request, todoID):
    task = Todo.objects.get(id=todoID)
    if request.method == 'POST':
        form = TodoForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponse('Edited Successfully')
    else:
        form = TodoForm(instance=task)
    return render(request, 'form.html', {'form': form})


def deleteTodo(request, todoID):
    todo = Todo.objects.get(id=todoID)
    todo.delete()
    return HttpResponse('Successfully deleted')

# def createTodo(request, todoID):
#     obj = Todo.objects.get(id=todoID)

#     if request.method == 'POST':
#         form = TodoForm(request.POST or None, instance=obj)
#         data = {
#             'form': form,
#         }
#         # details = TodoForm(request.POST)
#         # check weather the form is valid
#         if form.is_valid():
#             post = form.save(commit=False)

#             post.save()
#             return HttpResponse('Seccessfully added the task')
#     else:
#         form = TodoForm()
#     return render(request, 'form.html', {'form': form})


# def editTodo(request, todoID):
#     task = Todo.objects.get(id=todoID)
#     form = TodoForm(instance=task)
#     data = {
#         'form': form,
#         'task': task,
#     }
#     return render(request, 'form.html', data)

# def deleteTodo(request, taskid):
#     task = Todo.objects.get(id=taskid)
#     if request.method == 'POST':
#         task.delete()
#         return HttpResponse(taskid, "is Deleted")
