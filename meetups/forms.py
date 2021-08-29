from django import forms
from .models import Participant


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Participant # takes the fields from the Participant model 
        fields = ['email'] # restricts which fields should be taken from the model
