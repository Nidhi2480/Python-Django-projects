# forms.py
from django import forms
from MovieAPP.models import Movies

class MoviesForm(forms.ModelForm):
    class Meta:
        model = Movies
        exclude = ['user'] 
