from django import forms 
from . import models 

class CreatePost(forms.ModelForm): 
    class Meta: 
        model = models.Communitie
        fields = ['name','description','slug', 'free','banner']