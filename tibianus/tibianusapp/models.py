from django.db import models
import requests
from typing import Union

# Create your models here.


class Rank(models.Model):

    rank = models.CharField(max_length=150, unique=True)
    rank_loyality_level_point = models.PositiveIntegerField(null=True)
    min_loyality_level_point = models.PositiveIntegerField(null=True)
    max_loyality_level_point = models.PositiveIntegerField(null=True)
    min_loyality_trade_point = models.PositiveIntegerField(null=True)
    max_loyality_trade_point = models.PositiveIntegerField(null=True)
    min_experience_permonster = models.PositiveIntegerField(null=True)
    max_experience_permonster = models.PositiveIntegerField(null=True)
    min_experience_pertask = models.PositiveIntegerField(null=True)
    max_experience_pertask = models.PositiveIntegerField(null=True)
    
    def __str__(self) -> str:
        return self.rank



class TaskType(models.Model):
    task_type = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.task_type

class TaskDifficulty(models.Model):
    task_difficulty = models.CharField(max_length = 50)
    min_level_gain = models.PositiveIntegerField(null=True)
    max_level_gain = models.PositiveIntegerField(null=True)
    min_trade_gain = models.PositiveIntegerField(null=True)
    max_trade_gain = models.PositiveIntegerField(null=True)

    def __str__(self) -> str:
        return self.task_difficulty


class Achievement(models.Model):
    achvievement_name = models.CharField(max_length=300, unique=True)
    achvievement_description = models.TextField()
    loyality_level_point = models.PositiveIntegerField(null=True)
    loyality_trade_point = models.PositiveIntegerField(null=True)

    def __str__(self) -> str:
        return self.achvievement_name 


class Task(models.Model):
    task_name = models.CharField(max_length=300, unique=True)
    task_description = models.TextField(null=True)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    task_difficulty = models.ForeignKey(TaskDifficulty,on_delete=models.CASCADE)
    task_achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.task_name


class Character(models.Model):

    character_name = models.CharField(max_length=100)
    rank_name = models.ForeignKey(Rank, on_delete=models.SET_NULL, null=True)
    loyality_level_point = models.PositiveIntegerField(null=True)
    loyality_trade_point = models.PositiveIntegerField(null=True)

    def __str__(self) -> str:
        return self.character_name


class CharacterAchievement(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    achievement_gain = models.DateField()

    def __str__(self) -> str:
        return f"{str(self.character)} -> {str(self.achievement)}"
   


class ActiveTask(models.Model): 

    character = models.OneToOneField(Character, on_delete=models.SET_NULL, null=True)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    added = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{str(self.character)} -> {str(self.task)}"


class Monster(models.Model):

    monster_name = models.CharField(max_length=250, unique=True)
    monster_exp = models.BigIntegerField()



    def __str__(self) -> str:
        return f"{str(self.monster_name)} -> {str(self.monster_exp)}"




