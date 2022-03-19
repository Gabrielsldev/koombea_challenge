from django import forms
from .models import csvFile

class csvFileForm(forms.ModelForm):
    class Meta:
        model = csvFile
        fields = ('name', 'file')