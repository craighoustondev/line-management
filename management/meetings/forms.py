from django import forms
from .models import Employee, Meeting

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
