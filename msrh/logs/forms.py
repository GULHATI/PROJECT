from django.contrib.auth.forms import AuthenticationForm
from django import forms
# If you don't do this you cannot use Bootstrap CSS


class LoginForm(AuthenticationForm):
    type_1 = 'HOD'
    type_2 = 'HR'
    type_3 = 'Supervisor'
    TYPE_CHOICES = (
        (type_1, u"HOD"),
        (type_2, u"HR"),
        (type_3,u"SUPERVISOR"))
    type = forms.ChoiceField(label="type" ,choices=TYPE_CHOICES)
    username = forms.CharField(label="Emp_ID", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


