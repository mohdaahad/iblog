from cProfile import label
from pyexpat import model
from django import forms
from .models import Post, activity,Comment,User_Additional_detail
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
class SignUpForm(UserCreationForm):
    password1=forms.CharField(label='Password' ,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Passwoed'}))
    password2=forms.CharField(label='Confirm password(again)',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Confirm password(again)'}     ))

    class Meta:
        model=User
        fields=['first_name','last_name','username','email']
        labels ={'first_name':  'Fast Name','last_name':'Last Name','email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control','placeholder': 'Username',}),'first_name':forms.TextInput(attrs={'class':'form-control','placeholder': 'First Name'}),'last_name':forms.TextInput(attrs={'class':'form-control','placeholder': 'Last Name'}),'email':forms.EmailInput(attrs={'class':'form-control','placeholder': 'Email*'}), }
        
class loginForm(AuthenticationForm):
  username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control','placeholder': 'Username'}))
  password = forms.CharField(label=_("Password"),strip=False ,widget=forms.PasswordInput(attrs={ 'class':'form-control','autocomplete':'current-password','placeholder': 'Password'}))
 



class CommentForm(forms.ModelForm):
    class Meta:
        model =Comment
        fields = ("text",'name')  
        widgets ={'text':forms.TextInput(attrs={'class':'form-control','placeholder': 'Comment','cols': 30, 'rows': 3}),'name':forms.HiddenInput()}
        labels={'text':''}

class PostForm(forms.ModelForm):
    class Meta:
        model =Post
        fields = ('image',"title",'category','content','user_id')  
        widgets ={
          'title':forms.TextInput(attrs={'class':'form-control1','placeholder': 'New post title here...','cols': 30, 'rows': 1 , }),
          'content':forms.Textarea(attrs={'class':'form-control1','placeholder': 'Write your post content here...','cols': 27, 'rows': 4 , 'style': 'font-size: 20px;',}),
          'user_id':forms.HiddenInput()
          }
        labels={'title':'','image' :'','url' :'','category' :'','content' :'',}


class User_Additional_detailForm(forms.ModelForm):
  class Meta:
    model=User_Additional_detail
    fields =('user_profile',)




class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))                           
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email',"first_name"]




class UpdateProfileForm(forms.ModelForm):
    user_profile = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    class Meta:
        model = User_Additional_detail
        fields = ['user_profile',]