# Generated by Django 4.0.4 on 2022-06-01 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tibianusapp', '0020_activetask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activetask',
            name='character',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tibianusapp.character'),
        ),
        migrations.AlterField(
            model_name='activetask',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tibianusapp.task'),
        ),
    ]
