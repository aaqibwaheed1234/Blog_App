from django import forms
from .models import Comment, CustomUser
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body','post']


class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['picture']