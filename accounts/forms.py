from django.contrib.auth.models import User
from django import forms
class userForm(forms.ModelForm):
    
    username = forms.CharField()
    password = forms.CharField()
    class Meta:
        model = User
        fields = ('username','password')