from django.http import HttpResponse
from django.shortcuts import render

from .models import Achievement, Rank, Task


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
