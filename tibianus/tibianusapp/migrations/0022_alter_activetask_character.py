# Generated by Django 4.0.4 on 2022-06-01 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tibianusapp', '0021_alter_activetask_character_alter_activetask_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activetask',
            name='character',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tibianusapp.character'),
        ),
    ]