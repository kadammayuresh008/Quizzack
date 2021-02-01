from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	Address=forms.CharField(max_length=100)
	Institution=forms.CharField(max_length=100)

	class Meta:
		model = User
		fields=['username','email','password1','password2','Address','Institution']


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields=['username','email']

class ProfileUpdateFrom(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']
			
