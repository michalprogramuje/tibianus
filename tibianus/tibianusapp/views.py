from ctypes import sizeof
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ActiveTasksForm, CompleteTaskForm
from django import forms
from .models import Achievement, ActiveTask, Monster, Rank, Task, Character, TaskDifficulty, TaskType
from django.contrib import messages
import random
from django.utils.safestring import mark_safe
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
                if task_difficulty_id.task_difficulty == 'Adept':
                    scout_task = TaskType.objects.get(task_type='Scout')
                    available_tasks = Task.objects.filter(task_type=scout_task)
                    randomed_index = random.randint(0, len(available_tasks)-1)
                    looted_task = available_tasks[randomed_index]
                    active_task = ActiveTask(character=char_object, task=looted_task)
                    end_message = f"Twoja ranga to {task_difficulty_id}. Losowanie tasków typu {scout_task}. Wylosowałeś task \'{looted_task}\'. Więcej szczegółów na jego temat znajdziesz w sekcji /tasks"
                    active_task.save()
                    messages.success(request, f'{end_message}. Powodzenia!')
                else:
                    rank_id = Rank.objects.get(rank=char_object.rank_name)
                    min_experience_permonster = rank_id.min_experience_permonster
                    max_experience_permonster = rank_id.max_experience_permonster 
                    min_experience_pertask = rank_id.min_experience_pertask
                    max_experience_pertask = rank_id.max_experience_pertask 
                    
                    get_monsters = Monster.objects.filter(monster_exp__range=(min_experience_permonster, max_experience_permonster))
                    experience = random.randint(min_experience_pertask, max_experience_pertask)
                    randomed_monster_index = random.randint(0, len(get_monsters)-1)
                    monster_choosen = get_monsters[randomed_monster_index]
                    count = int(experience / monster_choosen.monster_exp)
                    task_name = f"Zabij {count} {monster_choosen.monster_name}"
                    task_exist = Task.objects.filter(task_name=task_name)
                    task_type_id = 1
                    task_description = f"Ten task to \'{task_name}\' Task dla rangi {rank_id.rank}. Powodzenia!"
                    end_message = f"Wylosowałeś task \'{task_name}\'. Ilość punktów doświadczenia per task jaką wylosowałeś wynosi {experience}. Ilość expa jaką daje wylosowany potwór wynosi {monster_choosen.monster_exp}. Sumarycznie masz do zabicia {count} {monster_choosen.monster_name}"
                    
                    if(task_exist):
                        new_active_task = ActiveTask(character=character_name, task=task_exist)
                        new_active_task.save()
                        messages.success(request, f'{end_message}. Powodzenia!')
                    else:
                        new_task = Task(task_name=task_name, task_difficulty_id=task_difficulty_id.id, task_type_id=task_type_id, task_description=task_description)
                        new_task.save()
                        new_active_task = ActiveTask(character=character_name, task=new_task)
                        new_active_task.save()
                        messages.success(request, f'{end_message}. Powodzenia!')
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
            
            
            if(ActiveTask.objects.get(character=character_name)):
                character = Character.objects.get(character_name=character_name)
                character_llp = character.loyality_level_point
                character_ltp = character.loyality_trade_point
                character_rank = character.rank_name
                rank = Rank.objects.get(rank=character_rank)
                min_loyality_level_point = rank.min_loyality_level_point
                max_loyality_level_point = rank.max_loyality_level_point
                min_loyality_trade_point = rank.min_loyality_trade_point
                max_loyality_trade_point = rank.max_loyality_trade_point
                random_loyality_level_point = random.randint(min_loyality_level_point, max_loyality_level_point)
                random_loyality_trade_point = random.randint(min_loyality_trade_point, max_loyality_trade_point)
                character.loyality_level_point = random_loyality_level_point + character_llp
                character.loyality_trade_point = random_loyality_trade_point + character_ltp
                                    # get_monsters = Monster.objects.filter(monster_exp__range=(min_experience_permonster, max_experience_permonster))
                character.save()
                character = Character.objects.get(character_name=character_name)
                character_points = character.loyality_level_point
                

                #  min_rank_loyality_level_point = models.PositiveIntegerField(null=True)
                #     max_rank_loyality_level_point = models.PositiveIntegerField(null=True)

                available_rank = Rank.objects.filter(max_rank_loyality_level_point__gte=character_points, min_rank_loyality_level_point__lte=character_points)

                if rank == available_rank[0]:
                    rank_message = f"Twoja ranga <strong>{rank}</strong> jest obecnie nadal aktualna.<br/>Realizuj kolejne zadania i zbieraj <strong>Loyality Level Points</strong> aby awansować do kolejnej rangi."
                else:
                    new_rank = Rank.objects.get(rank=available_rank[0])
                    character.rank_name = new_rank

                    rank_message = f"Gratulacje!<br/>Uzbierałeś wystarczającą ilość Loyality Level Points co sprawia, że awansujesz do wyższej rangi!<br/>Twoja ranga <strong>\'{rank}\'</strong> zmieniła się na <strong>\'{new_rank}\'</strong>."
                
                character.save()

                character_current_llp = character.loyality_level_point
                character_current_ltp = character.loyality_trade_point

                active_task = ActiveTask.objects.get(character=character)
                messages.success(request, mark_safe(f"Gratulacje!<br/> <strong>{character.character_name}</strong> ukończył zadanie <strong>\'{active_task.task.task_name}\'</strong>. <br/> Uzyskano <strong>{random_loyality_level_point} LLP</strong> oraz <strong>{random_loyality_trade_point} LTP</strong>.<br/>Łącznie posiadasz <strong>{character_current_llp} LLP</strong> oraz <strong>{character_current_ltp} LTP</strong>.<br/><br/><br/>{rank_message}"))
                active_task.delete()
        else:
            messages.error(request, f'{character_name} nie posiada obecnie żadnych zadań.')

    form = CompleteTaskForm()
    
    return render(request, 'complete-the-task/index.html', {'form': form})    
