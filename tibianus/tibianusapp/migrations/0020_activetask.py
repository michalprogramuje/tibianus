# Generated by Django 4.0.4 on 2022-06-01 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tibianusapp', '0019_task_task_achievement'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateField()),
                ('character', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tibianusapp.character')),
                ('task', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tibianusapp.task')),
            ],
        ),
    ]