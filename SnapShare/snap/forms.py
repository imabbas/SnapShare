from django.contrib.auth.models import User
from django import forms
from .models import Post


class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "email", "password"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {"user", "likes", "image", "comment"}
