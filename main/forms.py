from django import forms
from .models import Lab


class LabForm(forms.ModelForm):
    # title = forms.CharField(max_length=100)
    # content = forms.CharField(max_length=200)
    # start_date = forms.DateField()
    # due_date = forms.DateField()

    class Meta:
        model = Lab
        fields = ['title', 'description', 'start_date', 'due_date']