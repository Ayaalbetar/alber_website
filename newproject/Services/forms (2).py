from django import forms
from .models import Person
class NewPersonForm(forms.ModelForm):

    class Meta:
        model =Person
        fields=['fname','pname','photo']
