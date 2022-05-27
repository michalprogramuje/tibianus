from django.db import models

# Create your models here.


class Rank(models.Model):

    rank = models.CharField(max_length=150, unique=True)

    def __str__(self) -> str:
        return self.rank


class Achievement(models.Model):
    achvievement_name = models.CharField(max_length=300, unique=True)
    achvievement_description = models.TextField()
    loyality_level_point = models.PositiveIntegerField(null=True)
    loyality_trade_point = models.PositiveIntegerField(null=True)

    def __str__(self) -> str:
        return self.achvievement_name 

class Character(models.Model):

    character_name = models.CharField(max_length=100)
    rank_name = models.OneToOneField(Rank, on_delete=models.SET_NULL, null=True)
    loyality_level_point = models.PositiveIntegerField(null=True)
    loyality_trade_point = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.character_name


class CharacterAchievement(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    achievement_gain = models.DateField()

    def __str__(self):
        return f"{str(self.character)} -> {str(self.achievement)}"
   


# Po głębszej analize - To narazie jest nam niepotrzebne 
# class LoyalityLevelPoint(models.Model):

#     character = models.OneToOneField(Character, on_delete=models.CASCADE, primary_key=True)
#     loyality_level_point = models.IntegerField()


#     def __str__(self):
#         return "%s => %s points" % (self.character, self.loyality_level_point)



# class LoyalityTradePoint(models.Model):

#     character = models.OneToOneField(Character, on_delete=models.CASCADE, primary_key=True)
#     loyality_trade_point = models.IntegerField()

#     def __str__(self):
#         return "%s => %s points" % (self.character, self.loyality_trade_point)


