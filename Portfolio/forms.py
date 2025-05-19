from django import forms
from .models import *

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'image']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'technology_stack', 'url', 'description']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your email'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'placeholder': 'Write your message here...'}),
        }