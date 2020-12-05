from .models import MyUser
from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60,help_text='Required. Add a valid email address')
    class Meta:
        model= MyUser
        fields=['organization_name','email','password1','password2']