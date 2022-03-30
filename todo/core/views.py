from django.shortcuts import render

from core.forms import TodoForm

# Create your views here.

def home(request): 
    form = TodoForm()
    return render(request,'home.html',{'forms':form})