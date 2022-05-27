from django.http import HttpResponse
from django.shortcuts import render

from .models import Achievement, Rank


# Create your views here.


def index(request):
    return HttpResponse("Hello, world bitches.")
    

def get_all_ranks(request): 

    ranks = Rank.objects.all()

    return render(request, 'ranks/index.html', {'ranks': ranks})

def get_all_achievements(request): 
    
    achievements = Achievement.objects.all()

    return render(request, 'achievements/index.html', {'achievements': achievements})
