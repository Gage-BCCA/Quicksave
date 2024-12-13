from django import forms 

from .models import Game
from accounts.models import ExtendedUserData


class UserPostForm(forms.Form):
    post_content = forms.CharField(widget=forms.Textarea)


class GameCreationForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'genre', 'blurb', 'description']


class UserProfileDataForm(forms.ModelForm):
    class Meta:
        model = ExtendedUserData
        fields = ["profile_pic", "headliner", "bio", "location"]

    def __init__(self, *args, **kwargs):
        super(UserProfileDataForm, self).__init__(*args, **kwargs)
        self.fields['profile_pic'].required = False
        self.fields['headliner'].required = False
        self.fields['bio'].required = False
        self.fields['location'].required = False