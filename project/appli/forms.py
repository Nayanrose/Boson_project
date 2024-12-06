from django import forms
from .models import *

class Datainput(forms.DateInput):
    input_type = 'date'

class CreatingForm(forms.ModelForm):
    class Meta:
        model = addproject
        fields = '__all__'

        widgets = {
            'start_date': Datainput(),
            'end_date': Datainput(),

        }

        labels = {
            "name": "Name",
            "descrption": "Description",
            'start_date': "Start Date",
            'end_date': 'End Date',
            'status':'Status'

        }