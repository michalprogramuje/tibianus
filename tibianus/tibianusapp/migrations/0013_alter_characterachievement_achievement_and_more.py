# Generated by Django 4.0.4 on 2022-05-27 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tibianusapp', '0012_alter_characterachievement_achievement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterachievement',
            name='achievement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tibianusapp.achievement'),
        ),
        migrations.AlterField(
            model_name='characterachievement',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tibianusapp.character', unique=True),
        ),
    ]
