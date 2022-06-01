from django import forms
from .models import Task, Character


class ActiveTasksForm(forms.Form):
    character = forms.ModelChoiceField(label='Postać', queryset=Character.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    task = forms.ModelChoiceField(label='Zadanie', queryset=Task.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))

