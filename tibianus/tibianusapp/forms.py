from django import forms
from .models import ActiveTask,  Character



class CompleteTaskForm(forms.Form):
    
    task = forms.ModelChoiceField(label='Task', queryset=ActiveTask.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))


class ActiveTasksForm(forms.Form):
    
    character = forms.ModelChoiceField(label='Postać', queryset=Character.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
