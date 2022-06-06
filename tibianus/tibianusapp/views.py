from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ActiveTasksForm, CompleteTaskForm
from django import forms
from .models import Achievement, ActiveTask, Rank, Task, Character, TaskDifficulty
from django.contrib import messages
import random
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
            if(ActiveTask.objects.filter(character=character_name)):
                messages.error(request, f'{character_name} posiada obecnie aktywne zadanie.')
            else:
                char_object = Character.objects.get(character_name=character_name)
                task_difficulty_id = TaskDifficulty.objects.get(task_difficulty=char_object.rank_name)
                tasks = Task.objects.filter(task_difficulty=task_difficulty_id)
                randomized_id = random.randint(0, len(tasks)-1)
                looted_task = tasks[randomized_id]
                new_active_task = ActiveTask(character=character_name, task=looted_task)
                new_active_task.save()
                messages.success(request, f'{character_name} wylosował zadanie \'{looted_task}\'. Powodzenia!')
                return HttpResponseRedirect('add-active-task')
    else:
        form = ActiveTasksForm()
    
    return render(request, 'active-tasks/add-active-task.html', {'form': form})
    

def complete_the_task(request):

    if request.method == 'POST':
        form = CompleteTaskForm(request.POST)
        
        if form.is_valid(): 
            character_name = form.cleaned_data['task'].character
            task = form.cleaned_data['task'].task
            print(task)
            
            
            # # if(ActiveTask.objects.get(character=character_name)):
                
            # #     active_task = ActiveTask.objects.get(character=character_name)
            # #     active_task_name = active_task.task

            # #     task = Task.objects.get(task_name=active_task_name)
            # #     task_difficulty_name = task.task_difficulty
            # #     task_difficulty_object = Rank.objects.get(rank=task_difficulty_name)
            # #     level_gain = random.randint(task_difficulty_object.min_loyality_level_point, task_difficulty_object.max_loyality_level_point)
            # #     trade_gain = random.randint(task_difficulty_object.min_loyality_trade_point, task_difficulty_object.max_loyality_trade_point)
            # #     print(level_gain)
            # #     print(trade_gain)
            # else:
            #     messages.error(request, f'{character_name} nie posiada obecnie żadnych zadań.')
            
            

            # active_task.delete()


    form = CompleteTaskForm()
    
    return render(request, 'complete-the-task/index.html', {'form': form})    

