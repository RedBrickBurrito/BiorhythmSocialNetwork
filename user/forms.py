from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=200)
    birthday = forms.DateField(
        widget=forms.SelectDateWidget(
            years=range(1980, 2022)
        )
    )
    image = forms.ImageField()

    class Meta:
        model = CustomUser
        fields = ('email','birthday','image')
        
