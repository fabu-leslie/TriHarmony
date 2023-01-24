from django import forms


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

class ChildForm(forms.Form):
    name = forms.CharField(max_length=255)

