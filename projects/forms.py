from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'category', 'description', 'skills_required', 'budget_type', 'budget_min', 'budget_max', 'deadline', 'location']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'e.g. Build a landing page for my business'}),
            'description': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Describe the project in detail...'}),
            'skills_required': forms.TextInput(attrs={'placeholder': 'e.g. HTML, CSS, JavaScript'}),
            'deadline': forms.DateInput(attrs={'type': 'date'}),
            'location': forms.TextInput(attrs={'placeholder': 'Nairobi / Remote'}),
        }
