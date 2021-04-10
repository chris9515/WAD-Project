from django.shortcuts import redirect, render
from django.views.generic import ListView, TemplateView, View
from .models import ToDoList
from .forms import TodoForm
from django.http import HttpResponseRedirect 


# Create your views here.
# class DailyPlanner(ListView):
#     model = ToDoList
#     template_name = 'dailyPlanner.html'
#     def get_queryset(self):
#         return ToDoList.objects.all()
def DailyPlanner(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todolist')
    lists = ToDoList.objects.all()
    return render(request, 'dailyPlanner.html', {"text": form, "list":lists})

def update_task(request, pk):
    task = ToDoList.objects.get(id=pk)
    form = TodoForm(instance=task)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("todolist")
    return render(request, "updateList.html", {"edit": form})

def delete_task(request, pk):
    task = ToDoList.objects.get(id=pk)
    task.delete()
    return redirect("todolist")

def delete_all(request):
    task = ToDoList.objects.all()
    task.delete()
    return redirect("todolist")