# Generated by Django 4.0.4 on 2022-05-30 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tibianusapp', '0017_taskdifficulty_tasktype_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_description',
            field=models.TextField(null=True),
        ),
    ]