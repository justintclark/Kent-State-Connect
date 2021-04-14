from django import forms
from django.forms import ModelForm
from .models import *

class UserInForum(forms.ModelForm):
    class Meta:
        model = user
        fields = "__all__"

class CreateInForum(forms.ModelForm):
    class Meta:
        model= forum
        fields = "__all__"
        widgets = { 'description': forms.Textarea(attrs={'cols':60, 'rows':10})} 

class CreateInDiscussion(ModelForm):
    class Meta:
        model= Discussion
        fields = "__all__"
        widgets = { 'discuss': forms.Textarea(attrs={'cols':60, 'rows':10})} 