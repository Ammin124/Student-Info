from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['studentNumber', 'firstName', 'lastName', 'email', 'studyField', 'gpa']
        labels ={
            'studentNumber':'Student Number',
            'firstName':'First Name',
            'lastName':'Last Name',
            'email':'Email',
            'studyField':'Study Of Field',
            'gpa':'CGPA'
        }

        widgets ={
            'studentNumber': forms.NumberInput(attrs={'class':'form-control'}),
            'firstName': forms.TextInput(attrs={'class':'form-control'}),
            'lastName': forms.TextInput(attrs={'class': "form-control"}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'studyField': forms.TextInput(attrs={'class':'form-control'}),
            'gpa': forms.NumberInput(attrs={'class':'form-control'})
        }