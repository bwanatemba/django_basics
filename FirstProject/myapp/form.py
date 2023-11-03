from django import forms
from myapp.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['FirstName', 'Lastname', 'Email', 'Age', 'Password']
