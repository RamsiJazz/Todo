from django.shortcuts import redirect, render

from core.forms import TodoForm
from core.models import Todo

# Create your views here.

def home(request): 
    form = TodoForm()
    todos = Todo.objects.all()
    if request.method == "POST":
        form= TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'home.html',{'forms':form, 'todo':todos})