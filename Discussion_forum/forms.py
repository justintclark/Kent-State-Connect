from django import forms
from django.forms import ModelForm
from .models import *

class CreateInForum(forms.ModelForm):
    class Meta:
        model= forum
        fields = "__all__"
        widgets = { 'description': forms.Textarea(attrs={'cols':60, 'rows':10})} 

class CreateInDiscussion(ModelForm):
    class Meta:
        model= Discussion
        fields = "__all__"