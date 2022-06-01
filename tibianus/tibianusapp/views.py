from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ActiveTasksForm
from django import forms
from .models import Achievement, ActiveTask, Rank, Task
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')


def get_all_ranks(request): 

    ranks = Rank.objects.all()

    return render(request, 'ranks/index.html', {'ranks': ranks})


def get_all_achievements(request): 
    
    achievements = Achievement.objects.all()

    return render(request, 'achievements/index.html', {'achievements': achievements})


def get_all_tasks(request):

    tasks = Task.objects.all()

    return render(request, 'tasks/index.html', {'tasks': tasks})


def get_all_active_tasks(request):

    active_tasks = ActiveTask.objects.all() 

    return render(request, 'active-tasks/index.html', {'active_tasks': active_tasks})


def add_active_task(request):

    if request.method == 'POST':
        form = ActiveTasksForm(request.POST)
        if form.is_valid(): 
            character_name = form.cleaned_data['character']
            task_name = form.cleaned_data['task']
            if(ActiveTask.objects.filter(character=character_name, task=task_name)):
                messages.error(request, f'Zadadanie o nazwie \'{task_name}\' jest już wybrane przez {character_name}. Ukończ je aby wybrać je ponownie.')
            elif(ActiveTask.objects.filter(character=character_name)):
                messages.error(request, f'{character_name} posiada obecnie aktywne zadanie.')
            else:
                new_active_task = ActiveTask(character=character_name, task=task_name)
                new_active_task.save()
                messages.success(request, f'Zadanie \'{task_name}\' został przydzielony dla {character_name} pomyślnie')
                return HttpResponseRedirect('add-active-task')
    else:
        form = ActiveTasksForm()
    
    return render(request, 'active-tasks/add-active-task.html', {'form': form})
    


    
