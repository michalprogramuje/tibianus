# Generated by Django 4.0.4 on 2022-06-06 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tibianusapp', '0025_monster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='monster_name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]