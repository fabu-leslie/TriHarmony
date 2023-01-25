from django import forms
from .models import Child, Specialist


class BehaviorForm(forms.Form):
    child = forms.CharField(max_length=255)
    behavior1 = forms.CharField(max_length=255)
    behavior1_intensity = forms.IntegerField()
    behavior1_frequency = forms.IntegerField()
    behavior2 = forms.CharField(max_length=255)
    behavior2_intensity = forms.IntegerField()
    behavior2_frequency = forms.IntegerField()
    behavior3 = forms.CharField(max_length=255)
    behavior3_intensity = forms.IntegerField()
    behavoir3_frequency = forms.IntegerField()
    notes = forms.CharField(max_length=255)

# ModelForm class - should auto generate fields for each field in model, will handle input validation and error handling.


class ChildForm(forms.ModelForm):
    class Meta:
        model= Child
        fields = ['name', 'age', 'dob', 'gender', 'specialist']

