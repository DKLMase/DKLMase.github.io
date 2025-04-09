from django import forms
from .models import DailyTask, TutorialSchedule, ClassSchedule
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import WellnessCheck

# Create DailyTask Form
class DailyTaskForm(forms.ModelForm):
    class Meta:
        model = DailyTask
        fields = ['name', 'description', 'day', 'date', 'time', 'reminder']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

# Create TutorialSchedule Form
class TutorialScheduleForm(forms.ModelForm):
    class Meta:
        model = TutorialSchedule
        fields = ['module', 'day', 'time', 'venue', 'reminder', 'is_online']
        widgets = {
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

# Create ClassSchedule Form
class ClassScheduleForm(forms.ModelForm):
    class Meta:
        model = ClassSchedule
        fields = ['module', 'day', 'time', 'venue', 'is_online']
        widgets = {
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

# User Registration Form
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# WellnessCheck Form
class WellnessCheckForm(forms.ModelForm):
    class Meta:
        model = WellnessCheck
        fields = ['mood', 'stress_level', 'tiredness_level', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
