# Generated by Django 4.0.4 on 2022-05-27 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tibianusapp', '0004_loyalitytradepoint'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='rank_name',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tibianusapp.rank'),
        ),
    ]
