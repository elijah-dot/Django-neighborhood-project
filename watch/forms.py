from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Posts

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['email','username','password1','password2']
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['email','username']
        
class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['profile_picture','bio']
        
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Posts
        fields = ['name','post','an_img']
        
