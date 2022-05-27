from django.contrib import admin
from .models import Achievement, Character, CharacterAchievement, Rank

# Register your models here.
admin.site.register([Character, Rank, Achievement, CharacterAchievement])
