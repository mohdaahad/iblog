from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
class SignUpForm(UserCreationForm):
    password1=forms.CharField(label='Password' ,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}     ))

    class Meta:
        model=User
        fields=['username','first_name','last_name','email',]
        labels ={'first_name':  'Fast Name','last_name':'Last Name','email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),'first_name':forms.TextInput(attrs={'class':'form-control'}),'last_name':forms.TextInput(attrs={'class':'form-control'}),'email':forms.EmailInput(attrs={'class':'form-control'}), }

class loginForm(AuthenticationForm):
  username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
  password = forms.CharField(label=_("Password"),strip=False ,widget=forms.PasswordInput(attrs={ 'class':'form-control','autocomplete':'current-password'}))