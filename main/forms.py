from django import forms
from .models import Lab, Todo
from django.forms import inlineformset_factory
# from django.contrib.admin.widgets import SelectDateWidget

class LabForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    start_date = forms.DateField()
    due_date = forms.DateField()

    class Meta:
        model = Lab
        fields = ['title', 'description', 'start_date', 'due_date']

    # def __init__(self, *args, **kwargs):
    #     super(LabForm, self).__init__(*args, **kwargs)
    #     self.fields['start_date'].widget = widgets.AdminSplitDateTime()
    #     self.fields['due_date'].widget = widgets.AdminSplitDateTime()

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['title']


TodoFormSet = inlineformset_factory(Lab, Todo, form=TodoForm)