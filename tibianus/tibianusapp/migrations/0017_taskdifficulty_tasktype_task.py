# Generated by Django 4.0.4 on 2022-05-30 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tibianusapp', '0016_rank_rank_loyality_level_point'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskDifficulty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_difficulty', models.CharField(max_length=50)),
                ('min_level_gain', models.PositiveIntegerField(null=True)),
                ('max_level_gain', models.PositiveIntegerField(null=True)),
                ('min_trade_gain', models.PositiveIntegerField(null=True)),
                ('max_trade_gain', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=300, unique=True)),
                ('task_difficulty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tibianusapp.taskdifficulty')),
                ('task_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tibianusapp.tasktype')),
            ],
        ),
    ]
