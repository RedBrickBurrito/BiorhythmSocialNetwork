from django import forms
from numpy import product
from datetime import date

from user.models import CustomUser

from .models import Event


class CreateEventForm(forms.ModelForm):
    date = forms.DateField(
        initial=date.today().strftime('%Y-%m-%d'),
        widget=forms.SelectDateWidget(
        ),         required=True
    )

    class Meta:
        model = Event
        fields = {'title', 'date'}

    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop('user', '')
    #     super(EventForm, self).__init__(*args, **kwargs)
    #     self.fields['user_defined_code'] = forms.ModelChoiceField(
    #         queryset=CustomUser.objects.filter(customuser=user))
