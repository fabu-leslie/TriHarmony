from django import forms
from .models import Behavior, Child


# class BehaviorForm(forms.Form):
#     child = forms.CharField(max_length=255)
#     behavior1 = forms.CharField(max_length=255)
#     behavior1_intensity = forms.IntegerField()
#     behavior1_frequency = forms.IntegerField()
#     behavior2 = forms.CharField(max_length=255)
#     behavior2_intensity = forms.IntegerField()
#     behavior2_frequency = forms.IntegerField()
#     behavior3 = forms.CharField(max_length=255)
#     behavior3_intensity = forms.IntegerField()
#     behavoir3_frequency = forms.IntegerField()
#     notes = forms.CharField(max_length=255)

class BehaviorForm(forms.ModelForm):
    FREQUENCY_CHOICES = [
        ('0', '(0) nonexistant'),
        ('1', '(1) virtually nonexistent (less than once a month, not worrisome)'),
        ('2', '(2) upper limit of normal/tolerable for a child of same approximate age'),
        ('3', '(3) a few times in the past week and almost every week in the past month'),
        ('4', '(4) a few times in the past week and EVERY single week in the past month'),
        ('5', '(5) many times in the past week and almost every week in the past month'),
        ('6', '(6) many times in the past week and EVERY single week in the past month'),
        ('7', '(7) several times per day (with breaks in-between incidents), almost every day'),
        ('8', '(8) several times per day (with breaks in-between incidents, EVERY single day'),
        ('9', '(9) constantly (it never stops, or stops briefly before restarting) almost every day'),
        ('10', '(10) constantly (it never stops, or stops briefly before restarting) EVERY single day')

    ]
    INTENSITY_CHOICES = [
        ('0', '(0) Behavior isn’t worrisome. There are no negative consequences imaginable'),
        ('1', '(1) Behavior is not worrisome. There are almost no negative consequences imaginable'),
        ('2', '(2) Upper limit of tolerable for a child of the same approximate age. Behavior is manageable, but frustrating'),
        ('3', '(3) Behavior is severe enough to worry you almost every time'),
        ('4', '(4) Behavior is severe enough to worry you EVERY single time'),
        ('5', '(5) You categorize this behavior as very serious almost every time'),
        ('6', '(6) You categorize this behavior as very serious EVERY single time. This behavior IS hurting the child or others when it happens'),
        ('7', '(7) You categorize this behaviors as alarmingly serious almost every time'),
        ('8', '(8) You categorize this behavior as alarmingly serious EVERY single time. There are more "bad days" than "good days" overall.'),
        ('9', '(9) You categorize this behavior as catastrophic because it was, or is potentially life-threatening'),
        ('10', '(10) A successful or thwarted suicidal or homicidal act has occurred, OR child was in some other life-threatening situation')

    ]

    class Meta:
        model = Behavior
        fields = ['behavior1', 'behavior1_details', 'behavior1_intensity', 'behavior1_frequency', 'behavior2', 'behavior2_details', 'behavior2_intensity', 'behavior2_frequency',
                  'behavior3', 'behavior3_details', 'behavior3_intensity', 'behavior3_frequency']
    behavior1_intensity = forms.ChoiceField(choices=INTENSITY_CHOICES)
    behavior1_frequency = forms.ChoiceField(choices=FREQUENCY_CHOICES)
    behavior2_intensity = forms.ChoiceField(choices=INTENSITY_CHOICES)
    behavior2_frequency = forms.ChoiceField(choices=FREQUENCY_CHOICES)
    behavior3_intensity = forms.ChoiceField(choices=INTENSITY_CHOICES)
    behavior3_frequency = forms.ChoiceField(choices=FREQUENCY_CHOICES)

# ModelForm class - should auto generate fields for each field in model, will handle input validation and error handling.

# for new client


class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['name', 'age', 'dob', 'gender', 'specialist']
