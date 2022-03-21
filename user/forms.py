from django import forms
from django.contrib.auth.forms import UserCreationForm
from numpy import product
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, required=True)
    birthday = forms.DateField(
        widget=forms.SelectDateWidget(
            years=range(1980, 2022)
        ),         required=True
    )
    image = forms.ImageField(required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'birthday', 'image')
