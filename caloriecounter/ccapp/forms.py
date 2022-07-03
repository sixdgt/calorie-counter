from django import forms

# import our custom models
from ccapp.models import AppUser

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        # if we need all fields of model
        # fields = "__all__"

        # for login we only require email and password
        fields = ('email', 'password')
        model = AppUser

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields = ('first_name', 'middle_name', 'last_name', 'contact', 'email',\
            'gender', 'dob', 'blood_group', 'password', 'address', 'major_health_issue')

        model = AppUser

    
# Anomalies
# Insertion, Deleition and Update