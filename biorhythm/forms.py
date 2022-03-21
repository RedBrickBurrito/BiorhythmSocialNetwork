from django import forms
from numpy import product

from user.models import CustomUser

from .models import Event


class CreateEventForm(forms.ModelForm):
    birthday = forms.DateField(
        widget=forms.SelectDateWidget(
            years=range(2022, 2100)
        ),         required=True
    )

    class Meta:
        model = Event
        fields = {'title', 'birthday'}

    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop('user', '')
    #     super(EventForm, self).__init__(*args, **kwargs)
    #     self.fields['user_defined_code'] = forms.ModelChoiceField(
    #         queryset=CustomUser.objects.filter(customuser=user))
