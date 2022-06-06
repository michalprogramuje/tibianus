from django.contrib import admin
from .models import Achievement, Character, CharacterAchievement, Rank, Task, TaskType, TaskDifficulty, ActiveTask, Monster

# Register your models here.
admin.site.register([
    Character, Rank, Achievement, CharacterAchievement, Task, TaskDifficulty, TaskType, ActiveTask, Monster
    ])
