# Generated by Django 4.0.4 on 2022-05-27 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tibianusapp', '0008_achievement_loyality_level_points_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='achievement',
            old_name='loyality_level_points',
            new_name='loyality_level_point',
        ),
        migrations.RenameField(
            model_name='achievement',
            old_name='loyality_trade_points',
            new_name='loyality_trade_point',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='achvievements',
            new_name='achvievement',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='loyality_level_points',
            new_name='loyality_level_point',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='loyality_trade_points',
            new_name='loyality_trade_point',
        ),
    ]