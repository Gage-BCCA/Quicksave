from django import forms 

from .models import Game


class UserPostForm(forms.Form):
    post_content = forms.CharField(widget=forms.Textarea)

class GameCreationForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'genre', 'blurb', 'description']