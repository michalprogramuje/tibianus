from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('ranks', views.get_all_ranks, name='get_all_ranks'),
    path('achvievements', views.get_all_achievements, name='get_all_achievements'),
    path('tasks', views.get_all_tasks, name='get_all_tasks')

]