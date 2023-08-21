from django import forms
from .models import Behavior, Child, BehaviorCheckIn, Feeling, Parent

FREQUENCY_CHOICES = [
    ('0', '(0) nonexistent'),
    ('1', '(1) virtually nonexistent (less than once a month, not worrisome)'),
    ('2', '(2) upper limit of normal/tolerable for a child of same approx. age'),
    ('3', '(3) a few times this past week and almost every week this past month'),
    ('4', '(4) a few times this past week and EVERY single week this past month'),
    ('5', '(5) many times this past week and almost every week this past month'),
    ('6', '(6) many times this past week and EVERY single week this past month'),
    ('7', '(7) several times per day, almost every day'),
    ('8', '(8) several times per day, EVERY single day'),
    ('9', '(9) constantly almost every day'),
    ('10', '(10) constantly EVERY single day')

]
INTENSITY_CHOICES = [
    ('0', '(0) Behavior isn’t worrisome. There are no negative consequences imaginable'),
    ('1', '(1) Behavior is not worrisome. There are almost no negative consequences imaginable'),
    ('2', '(2) Upper limit of tolerable. Behavior is manageable, but frustrating'),
    ('3', '(3) Severe enough to worry you almost every time'),
    ('4', '(4) Severe enough to worry you EVERY single time'),
    ('5', '(5) Very serious almost every time'),
    ('6', '(6) Very serious EVERY single time and is hurting the child or others when it happen'),
    ('7', '(7) Alarmingly serious almost every time'),
    ('8', '(8) Alarmingly serious EVERY time and there are more "bad days" than "good days" overall'),
    ('9', '(9) This behavior is or was potentially life-threatening'),
    ('10', '(10) Behavior has been life-threatening')

]


class FeelingForm(forms.ModelForm):
    feeling = forms.ChoiceField(
        choices=Feeling.FEELINGS_CHOICES, widget=forms.RadioSelect(), required=True)
    note = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Feeling
        fields = ['feeling', 'note']

    def clean(self):
        cleaned_data = super().clean()
        feeling = cleaned_data.get('feeling')

        if not feeling:
            raise forms.ValidationError('Please select a feeling!')

        return cleaned_data


class BehaviorForm(forms.ModelForm):
    class Meta:
        behavior_choices = Behavior.objects.all()
        model = BehaviorCheckIn
        fields = ['behavior', 'behavior_intensity',
                  'behavior_frequency', 'note']
        widgets = {
            'behavior': forms.Select(choices=behavior_choices, attrs={'class': 'form-control', 'required': True, }),
            'behavior_intensity': forms.Select(choices=INTENSITY_CHOICES, attrs={'class': 'form-control', 'required': True, }),
            'behavior_frequency': forms.Select(choices=FREQUENCY_CHOICES, attrs={'class': 'form-control', 'required': True, }),
            'note': forms.Textarea(attrs={'class': 'form-control', 'required': False}),
        }

    # def __init__(self, child, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['behavior'].queryset = Behavior.objects.filter(child=child)
# ModelForm class - should auto generate fields for each field in model, will handle input validation and error handling.


class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['name', 'age', 'dob', 'gender', 'specialist']


class SpecialistBehaviorForm(forms.ModelForm):
    class Meta:
        model = Behavior
        fields = ['behavior', 'behavior_details', 'notes']
        widgets = {
            'behavior': forms.Textarea(attrs={'class': 'form-control col-md-6', 'rows': 1}),
            'behavior_details': forms.Textarea(attrs={'class': 'form-control col-md-6', 'rows': 3}),
            'notes': forms.Textarea(attrs={'class': 'form-control col-md-6', 'rows': 5, 'required': False}),
        }


class CustomParentForm(forms.ModelForm):
    children = forms.ModelMultipleChoiceField(
        queryset=Child.objects.all(),  # Customize the queryset as needed
        widget=forms.CheckboxSelectMultiple,
        required=False  # Adjust as needed
    )

    class Meta:
        model = Parent
        fields = '__all__'
