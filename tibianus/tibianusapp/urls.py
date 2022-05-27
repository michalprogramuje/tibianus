from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('ranks', views.get_all_ranks, name='get_all_ranks'),
    path('achvievements', views.get_all_achievements, name='get_all_achievements')

]