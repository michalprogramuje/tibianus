# Generated by Django 4.0.4 on 2022-05-27 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tibianusapp', '0010_remove_character_achvievement_characterachievements'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CharacterAchievements',
            new_name='CharacterAchievement',
        ),
    ]
