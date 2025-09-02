from django.shortcuts import render
from django.http import HttpResponseRedirect

from todo_app.models import Todo
from todo_app import views
  

def todo_list(request):
    todos = Todo.objects.all() #quertSet / ORM
    return render(
        request,
        "todo_list.html",
        {"todos": todos}

    )

def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return HttpResponseRedirect("/")

def todo_create(request):
    
    if request.method == "GET":
        return render(request, "todo_create.html")
    else:
        Todo.objects.create(title=request.POST['Title'])
        return HttpResponseRedirect("/")

