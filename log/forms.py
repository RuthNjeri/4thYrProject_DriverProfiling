#log/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm 
from .models import UserProfile
from .models import User


# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

class ProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('business_name','email','location','phone_number','role')
		widgets ={
			'business_name':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.TextInput(attrs={'class':'form-control'}),
			'location':forms.TextInput(attrs={'class':'form-control'}),
			'phone_number':forms.TextInput(attrs={'class':'form-control'}),
			'role':forms.TextInput(attrs={'class':'form-control'})
		}
		