# Generated by Django 4.0.4 on 2022-05-30 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tibianusapp', '0018_task_task_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_achievement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tibianusapp.achievement'),
        ),
    ]
